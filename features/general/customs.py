import discord
from discord import Embed
from discord.ext.commands import (
    Cog,
    group,
    command,
    Context,
)
from modules.margiela import Margiela
from workers.client import Emoji, Color


class AutoWorker(Cog):
    def __init__(self: "AutoWorker", bot: Margiela, *args, **kwargs) -> None:
        self.bot = bot

    class ButtonWorker:

        """
        This is a custom class for my buttons for the auto pfp
        """

        async def edgy(interaction: discord.Interaction) -> discord.Interaction:
            return interaction.response.edit_message("L", view=None)

    @group(
        name="autopfp",
        usage="(Channel) <Category> # Automatic Custom Setup",
        invoke_without_command=True,
        aliases=[
            "pfp",
            "post",
            "autopost",
        ],
    )
    async def _autopfp(self: "AutoWorker", ctx: Context) -> None:
        ...

    @_autopfp.command(
        name="setup",
        usage="(Channel)",
        aliases=[
            "startup",
            "build",
            "start",
            "create",
        ],
    )
    async def _startautopfp(
        self: "AutoWorker",
        ctx: Context,
        channel: discord.TextChannel | discord.Thread,
    ) -> None:
        """
        Buttons
        """
        edgy = discord.ui.Button(
            label="Edgy",
            style=discord.ButtonStyle.blurple,
            emoji=Emoji.bow,
        )
        females = discord.ui.Button(
            label="Females",
            style=discord.ButtonStyle.blurple,
            emoji=Emoji.bunny,
        )
        soft = discord.ui.Button(
            label="Soft",
            style=discord.ButtonStyle.blurple,
            emoji=Emoji.chika,
        )
        world = discord.ui.Button(
            label="World",
            style=discord.ButtonStyle.blurple,
            emoji=Emoji.melody,
        )
        edgy.callback = AutoWorker.ButtonWorker.edgy
        females.callback = AutoWorker.ButtonWorker.edgy
        soft.callback = AutoWorker.ButtonWorker.edgy
        world.callback = AutoWorker.ButtonWorker.edgy
        view = discord.ui.View()
        view.add_item(edgy)
        view.add_item(females)
        view.add_item(soft)
        view.add_item(world)

        """
        Sending & Calling the Embed out
        """
        await ctx.send(
            embed=Embed(
                title="Auto Post Configuration",
                description=(
                    f"> Please choose an auto post category to post in this channel\n"
                    f"> You **__cannot__** have one channe post all of the categories\n"
                    f"Need Help? you can [`Check this Documentation`](https://docs.com/) for problems with this"
                ),
                color=Color.blue,
            )
            .set_image(
                url="https://cdn.discordapp.com/attachments/1140433273064001546/1141524203233869844/main_gridblocks.png"
            )
            .set_author(
                name="Post Worker Setup", icon_url=ctx.author.display_avatar.url
            ),
            view=view,
        )


async def setup(bot):
    await bot.add_cog(AutoWorker(bot))
