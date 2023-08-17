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

    @command(name="instagram", usage="(Username)", aliases=["ig"])
    async def instagram(self: "AutoWorker", ctx: Context, user: str = None):
        if not user:
            return await ctx.failure(
                "Slow down buddy... you cant run this without a user!"
            )
        data = self.bot.session.get(
            self=self,
            url="https://dev.lains.life/instagram/profile",
            params={"username": user},
        )
        return data

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

        async def edgycallback(interaction: discord.Interaction) -> None:
            check = await self.bot.db.fetch(
                """
                SELECT * FROM AutoWorker
                WHERE Channel = $1
                """,
                channel.id,
            )
            if check:
                return await ctx.failure(
                    "There is already a **running worker** for this channel."
                )
            else:
                await self.bot.db.execute(
                    """
                    INSERT INTO AutoWorker (Guild, Channel, Category)
                    VALUES ($1, $2, $3)
                    """,
                    ctx.guild.id,
                    channel.id,
                    "Edgy",
                )
                await interaction.response.edit_message(
                    embed=Embed(
                        description=(
                            f"Created a new **Post Task** for {channel.mention}.\n"
                            f"> Margiela will now post **Edgy** pfps for now on.\n"
                            f"> This will now scrape new pfps posted on these platforms:\n"
                            f"[`pintrest.com`](https://pintrest.com)"
                            f"[`weheart.it`](https://weheart.it)"
                            f"[`discord.gg/pfps`](https://discord.gg/pfps)"
                        ),
                        color=Color.blue,
                    ),
                    view=None,
                )

        edgy.callback = AutoWorker.edgycallback(
            interaction=discord.Interaction,
        )
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
                    f"> You **__cannot__** have one channel post all of the categories\n"
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
