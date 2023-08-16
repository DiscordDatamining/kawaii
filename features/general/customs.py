from discord import Embed
from discord.ext.commands import (
    Cog,
    group,
    command,
)
from modules.margiela import Margiela


class AutoWorker(Cog):
    def __init__(self: "AutoWorker", bot: Margiela, *args, **kwargs) -> None:
        self.bot, self.client, self.worker = bot


async def setup(bot: Margiela) -> None:
    await bot.add_cog(AutoWorker(bot))
