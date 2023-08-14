import os
import discord
import aiohttp

from workers.client import Authorization
from workers.manager import Manager
from discord.ext.commands import (
    AutoShardedBot,
)


class Kawaii(AutoShardedBot):
    def __init__(
        self: "Kawaii",
        *args,
        **kwargs,
    ) -> None:
        super().__init__(
            strip_after_prefix=True,
            case_insensitive=True,
            command_prefix=Authorization.prefix,
            help_command=None,
            max_messages=5000,
            intents=discord.Intents.all(),
            allowed_mentions=discord.AllowedMentions(
                everyone=False,
                roles=False,
                users=True,
                replied_user=False,
            ),
            activity=discord.Activity(
                type=discord.ActivityType.competing,
                name="Your mum",
            ),
            owner_ids=Authorization.owner_ids,
        )

    async def on_connect(self: "Kawaii") -> None:
        self.ready = True
        self.session = aiohttp.ClientSession()
        if self.ready is not True:
            return 0
        else:
            pass
        await self.load_extension("jishaku")
