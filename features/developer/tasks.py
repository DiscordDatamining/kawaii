import subprocess
import discord
from discord import Embed
from discord.ext.commands import (
    Cog,
    command,
    is_owner,
    Context,
)
from modules.margiela import Margiela


class Tasks(Cog):
    def __init__(self: "Tasks", bot: Margiela, *args, **kwargs) -> None:
        """
        Sets up tasks for the backend of the bot
        """
        self.bot = bot
        self.worker_count: int = 0

    @command(name="pull")
    @is_owner()
    async def pull(
        self: "Tasks",
        ctx: Context,
    ) -> None:
        try:
            result = subprocess.check_output(
                ["git", "pull", "origin", "main"], stderr=subprocess.STDOUT, text=True
            )
            await ctx.dispatch(
                "[`git pull origin main | approved | PM2 RESTARTING`](https://github.com/DiscorDatamining/kawaii)\n"
                "```sh\n"
                f"{result}```\n "
            )
        except subprocess.CalledProcessError as e:
            await ctx.failure(
                f"[`Failed to pull branch`](https://github.com/DiscorDatamining/kawaii)\n{e}."
            )
        subprocess.check_output(
            [
                "pm2",
                "restart",
                "all",
            ],
            stderr=subprocess.STDOUT,
            text=True,
        )


async def setup(bot):
    await bot.add_cog(Tasks(bot))
