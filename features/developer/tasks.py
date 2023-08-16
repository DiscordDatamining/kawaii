import os
from discord import Embed
from discord.ext.commands import (
    Cog,
    command,
    is_owner,
    Context,
)
from modules.kawaii import Kawaii


class Tasks(Cog):
    def __init__(self: "Tasks", bot: Kawaii, *args, **kwargs) -> None:
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
        terminal = os.system("git pull origin main")
        await ctx.dispatch(
            "[`git pull origin main|approved`](https://github.com/DiscorDatamining/kawaii)\n"
            "```sh\n"
            f"{terminal}\n"
            "```"
        )


async def setup(bot):
    await bot.add_cog(Tasks(bot))
