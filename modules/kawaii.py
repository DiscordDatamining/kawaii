import os

import discord
from aiohttp import ClientSession
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
from workers.paginator import Paginator


class Kawaii(Bot):
    def __init__(self: "Kawaii") -> None:
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
                name="wewe",
                state="you know me? im kawaii :3",
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

    async def setup_hook(self: "Kawaii") -> None:
        try:
            self.db = await Manager.create_task(
                host="db.vdukveeoxwifoqdketql.supabase.co",
                user="postgres",
                port=5432,
                database="postgres",
                password="101908tjmmm4",
            )
            self.ready = True
        except Exception as e:
            raise e
        pass

    async def on_ready(self: "Kawaii") -> None:
        await self.load_extension("jishaku")
        for root, dirs, files in os.walk("features"):
            for filename in files:
                if filename.endswith(".py"):
                    cog_name = os.path.join(root, filename)[:-3].replace(os.sep, ".")
                    try:
                        await self.load_extension(cog_name)
                    except:
                        pass

    async def get_context(
        self: "Kawaii", message: discord.Message, *, cls=None
    ) -> None:
        """
        Gets the context, and then returns it
        """
        return await super().get_context(message, cls=cls or Kawaii.context)

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
            self: "Kawaii.context", message: str, error_code: str = None
        ) -> None:
            if not error_code:
                self.callbacks = False
            else:
                """
                Still returns dispatch as true even if no error_code was given
                """
            await self.send(
                embed=Embed(
                    description=f"{Emoji.bow} {self.author.mention}, {message}",
                    color=Color.normal,
                )
            )

        async def failure(
            self: "Kawaii.context", message: str, error_code: str = None
        ) -> None:
            if not error_code:
                self.callbacks = False
            else:
                """
                Still returns dispatch as true even if no error_code was given
                """
            await self.send(
                embed=Embed(
                    description=f"{Emoji.bunny} {self.author.mention}, {message} :c",
                    color=Color.error,
                )
            )
