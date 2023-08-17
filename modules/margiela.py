import os

import discord
from aiohttp import ClientSession
from asyncpg import create_pool
from discord import Embed, Intents
from discord.ext.commands import (
    ArgumentParsingError,
    Bot,
    CommandError,
    Context,
    MissingPermissions,
)

from workers.client import Authorization, Color, Emoji, Task
from workers.manager import Manager
from workers.paginator import Paginator as pg


class Margiela(Bot):
    def __init__(self: "Margiela") -> None:
        allowed_mentions = discord.AllowedMentions(
            everyone=False,
            users=True,
            roles=True,
            replied_user=False,
        )
        super().__init__(
            intents=Intents.all(),
            command_prefix=Authorization.prefix,
            allowed_mentions=allowed_mentions,
            owner_ids=Authorization.owner_ids,
            help_command=None,
            case_insensitive=True,
            strip_after_prefix=True,
            max_messages=1500,
            status=discord.Status.idle,
            activity=discord.Activity(
                type=discord.ActivityType.custom,
                name="|||||||",
                state="<3",
            ),
        )
        """
        Getting the bot ready for other events
        Example:
            If True, it'll return if its True or False
            False: it'll stop the other workers and stop the bot
            True: it'll start the other managers for the auto pfps etc
        """
        self.overload = False
        self.callbacks = True
        self.ready = False

    async def setup_hook(self: "Margiela") -> None:
        try:
            self.db = await create_pool(
                **{
                    "host": "db.vdukveeoxwifoqdketql.supabase.co",
                    "user": "postgres",
                    "port": 5432,
                    "database": "postgres",
                    "password": "101908tjmmm4",
                }
            )
            self.ready = True
        except Exception as e:
            raise e
        pass

    async def on_ready(self: "Margiela") -> None:
        await self.load_extension("jishaku")
        for root, dirs, files in os.walk("features"):
            for filename in files:
                if filename.endswith(".py"):
                    cog_name = os.path.join(root, filename)[:-3].replace(os.sep, ".")
                    try:
                        await self.load_extension(cog_name)
                        print(f"{cog_name} has been granted")
                    except:
                        pass

    async def get_context(
        self: "Margiela", message: discord.Message, *, cls=None
    ) -> None:
        """
        Gets the context, and then returns it
        """
        return await super().get_context(message, cls=cls or Margiela.context)

    class context(Context):
        """
        Custom context
        Examples:
            (Dispatch): string|int -> 'await ctx.dispatch("Message")'
            (Warning|Error|Failure): string -> 'await ctx.callback("Message")'
            (Overload): None -> ...
            (Pagination): List -> ...
        """

        async def dispatch(
            self: "Margiela.context", message: str = None, error_code: str = None
        ) -> None:
            if not error_code:
                self.callbacks = False
            else:
                """
                Still returns dispatch as true even if no error_code was given
                """
            await self.send(
                embed=Embed(
                    description=f"{message}",
                    color=Color.normal,
                )
            )

        async def approve(self: "Margiela.context", message: str) -> None:
            await self.send(
                embed=Embed(
                    description=f"{Emoji.approve} {self.author.mention}, {message}",
                    color=Color.approve,
                )
            )

        async def failure(
            self: "Margiela.context", message: str = None, error_code: int = None
        ) -> None:
            if not error_code:
                self.callbacks = False
            elif error_code:
                return await self.send(
                    embed=Embed(
                        description=f"{Emoji.warn} {self.author.mention}, An **[`{error_code}`](https://http.cat/{error_code})** error occured while performing this task",
                        color=Color.warning,
                    )
                )
            else:
                """
                Still returns dispatch as true even if no error_code was given
                """
            await self.send(
                embed=Embed(
                    description=f"{Emoji.warn} {self.author.mention}, {message} ",
                    color=Color.warning,
                )
            )

        async def paginate(
            self: "Margiela.context", ctx: Context, embeds: list, *args, **kwargs
        ) -> None:
            page = pg(
                self.bot,
                embeds,
                ctx,
                invoker=ctx.author.id,
            )
            page.add_button(
                "prev",
                emoji=Emoji.left,
                style=discord.ButtonStyle.blurple,
            )
            page.add_button(
                "next",
                emoji=Emoji.right,
                style=discord.ButtonStyle.blurple,
            )
            page.add_button(
                "goto",
                emoji=Emoji.goto2,
                style=discord.ButtonStyle.gray,
            )
            page.add_button(
                "delete",
                emoji=Emoji.cancel,
                style=discord.ButtonStyle.danger,
            )
            return await page.start()
