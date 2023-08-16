import discord
from discord import Embed
from discord.ui import View
from discord.ext.commands import (
    Cog,
    Context,
    group,
    command,
)
from modules.kawaii import Kawaii
from workers.client import Emoji, Color
from workers.manager import Manager


class Worker(Cog):
    def __init__(self: "Worker", bot: Kawaii, *args, **kwargs) -> None:
        self.bot, self.client = bot


async def setup(bot):
    await bot.add_cog(Worker(bot))
