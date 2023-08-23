import discord
from discord import Embed
from discord.ext.commands import (
    Cog,
    group,
    command,
    Context,
)
import random
import string
from modules.margiela import Margiela
from workers.client import Emoji, Color


class AutoWorker(Cog):
    def __init__(self: "AutoWorker", bot: Margiela, *args, **kwargs) -> None:
        self.bot = bot

    @command(
        name="exchange",
        aliases=["start"],
    )
    async def exchange(
        self: "AutoWorker",
        ctx: Context,
        amount=None,
    ) -> None:
        """
        Sets up purchases for PayPal to Cash App Exchanges
        """
        PayPal = discord.ui.Button(
            label="PayPal to Cashapp",
            style=discord.ButtonStyle.blurple,
        )
        Cashapp = discord.ui.Button(
            label="Cash App to PayPal",
            style=discord.ButtonStyle.green,
        )
        Support = discord.ui.Button(
            label="Create a Support Thread",
            style=discord.ButtonStyle.gray,
        )

        async def PayPal_callback(interaction: discord.Interaction) -> None:
            """
            PayPal Callback
            """
            if interaction.user != interaction.user:
                return
            note = "heheheheheheh"
            return await interaction.response.send_message(
                embeds=[
                    discord.Embed(
                        description=(
                            f"> Please send ${amount} to [`@forbiddenwillows`](https://paypal.me/forbiddenwillows) on PayPal.\n"
                            f"> Use the note `{note}` in the PayPal transaction for it to be verified.\n"
                            f"This transaction will take up to **160** Seconds to identify.\n"
                            f"Contact a Staff member if this transaction fails."
                        ),
                        color=0x080808,
                    ),
                    discord.Embed(
                        title="PayPal QR Code",
                        description="> Scan the QR Code below to pay!",
                        color=0x00ABC9,
                    ),
                ],
                ephemeral=True,
            )

        PayPal.callback = PayPal_callback
        view = discord.ui.View()
        view.add_item(PayPal)
        view.add_item(Cashapp)
        view.add_item(Support)
        await ctx.send(
            content=(
                f"Please select a method you would like to exchange.\n"
                f"This message will Self-destruct in [`Less than a minute`](<https://discord.com/tos>)\n"
                f"If your transaction isnt identified, Contact a Moderator or Staff."
            ),
            view=view,
        )

    @group(
        name="autopfp",
        usage="(Channel) <Category> # Automatic Custom Setup ",
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
                return await interaction.response.edit_message(
                    embed=Embed(
                        description=f"{Emoji.warn} {interaction.user.mention}, There is already a **running worker** for this channel.",
                        color=Color.warning,
                    )
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
                            f"Margiela will now post **Edgy** pfps for now on.\n"
                            f"This will now scrape new pfps posted on these platforms:\n"
                            f"> [`pintrest.com`](https://pintrest.com)\n"
                            f"> [`weheart.it`](https://weheart.it)\n"
                            f"> [`discord.gg/pfps`](https://discord.gg/pfps)\n"
                        ),
                        color=Color.blue,
                    ),
                    view=None,
                )

        edgy.callback = edgycallback
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
