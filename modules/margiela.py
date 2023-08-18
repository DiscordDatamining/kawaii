import os
import sys

import discord
from aiohttp import ClientSession
from asyncpg import create_pool
from discord.gateway import DiscordWebSocket
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
            activity=discord.Activity(
                type=discord.ActivityType.custom,
                state="Discord Activities",
                name=".",
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

    async def identify(self):
        payload = {
            "op": self.IDENTIFY,
            "d": {
                "token": self.token,
                "properties": {
                    "$os": sys.platform,
                    "$browser": "Discord iOS",
                    "$device": "Discord iOS",
                    "$referrer": "",
                    "$referring_domain": "",
                },
                "compress": True,
                "large_threshold": 250,
                "v": 3,
            },
        }

        if self.shard_id is not None and self.shard_count is not None:
            payload["d"]["shard"] = [self.shard_id, self.shard_count]

        state = self._connection
        if state._activity is not None or state._status is not None:
            payload["d"]["presence"] = {
                "status": state._status,
                "game": state._activity,
                "since": 0,
                "afk": False,
            }

        if state._intents is not None:
            payload["d"]["intents"] = state._intents.value

        await self.call_hooks(
            "before_identify", self.shard_id, initial=self._initial_identify
        )
        await self.send_as_json(payload)

    DiscordWebSocket.identify = identify

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
                    description=f"> 🦅 {self.author.mention}, {message}",
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
                        description=f"> 🦅 {self.author.mention}, An **[`{error_code}`](https://http.cat/{error_code})** error occured while performing this task",
                        color=Color.error,
                    )
                )
            else:
                """
                Still returns dispatch as true even if no error_code was given
                """
            await self.send(
                embed=Embed(
                    description=f"> 🦅 {self.author.mention}, {message} ",
                    color=Color.error,
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
                label="Previous",
                style=discord.ButtonStyle.blurple,
            )
            page.add_button(
                "next",
                emoji=Emoji.right,
                label="Next",
                style=discord.ButtonStyle.blurple,
            )
            page.add_button(
                "delete",
                emoji=Emoji.cancel,
                label="Delete",
                style=discord.ButtonStyle.danger,
            )
            return await page.start()
