import os

import discord
from discord import Embed, Intents
from discord.ext.commands import (
    ArgumentParsingError,
    Bot,
    CommandError,
    Context,
    MissingPermissions,
)
from aiohttp import ClientSession
from workers.client import Authorization
from workers.manager import Manager


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
                state=":smiley: pfps! :3",
            ),
        )
        """
        Getting the bot ready for other events
        Example:
            If True, it'll return if its True or False
            False: it'll stop the other workers and stop the bot
            True: it'll start the other managers for the auto pfps etc
        """
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
