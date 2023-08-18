import discord
from modules.margiela import Margiela
from discord.ext.commands import (
    Cog,
    group,
    command,
    Context,
)


class Welcome(Cog):
    def __init__(self: "Welcome", bot: Margiela, *args, **kwargs) -> None:
        self.bot: Margiela = bot

    @group(
        name="welcome",
        usage="(Channel) (Message) <Flags>",
        aliases={
            "welc",
            "wlc",
        },
    )
    async def welcome(
        self: "Welcome",
        ctx: Context,
    ) -> None:
        pass
