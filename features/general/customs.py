from discord import Embed
from discord.ext.commands import (
    Cog,
    group,
    command,
)


class AutoWorker(Cog):
    def __init__(self: "AutoWorker", bot, *args, **kwargs) -> None:
        self.bot, self.client, self.worker = bot


async def setup(bot):
    await bot.add_cog(AutoWorker(bot))