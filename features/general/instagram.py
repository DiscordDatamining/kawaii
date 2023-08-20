import discord
from discord import Embed
from discord.ext.commands import (
    Cog,
    group,
    command,
    Context,
)
from modules.margiela import Margiela


class InstagramTask(Cog):
    def __init__(self: "InstagramTask", bot: Margiela, *args, **kwargs) -> None:
        self.bot: Margiela = bot

    @group(
        name="instagram",
        usage="(Command) <...>",
        invoke_without_command=True,
        aliases=["ig"],
    )
    async def instagram(
        self: "InstagramTask",
        ctx: Context,
        *args,
        **kwargs,
    ) -> None:
        ...

    @instagram.command(
        name="follow",
        aliases=["bot"],
    )
    async def followbot(
        self: "InstagramTask", ctx: Context, username: str = None
    ) -> None:
        if not username:
            return await ctx.failure(
                "Could not start a proper **Instagram Follow Task**"
            )


async def setup(bot):
    await bot.add_cog(InstagramTask(bot))
