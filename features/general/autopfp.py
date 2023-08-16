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

    class Callback:
        def __init__(self: "Worker.Callback", *args, **kwargs) -> None:
            pass

        """
        These are special callbacks for the buttons
        Example: I Will call this class for my view points
            -> await Worker.Callback.<viewpoint>()
            -> await Worker.Callback.ButtonName()
        """

        async def setupautopfp(
            self: "Worker.Callback", interaction: discord.Interaction
        ) -> None:
            if not interaction.user != interaction.user:
                return await Worker.bot.ext.failure("FaiL?")

    @command(name="what")
    async def what(self: "Worker", ctx: Context) -> None:
        yes = discord.ui.Button(emoji=Emoji.bunny)
        yes.callback = Worker.Callback.setupautopfp
        view = View()
        view.add_item(yes)
        await ctx.send("hello", view=view)


async def setup(bot):
    await bot.add_cog(Worker(bot))
