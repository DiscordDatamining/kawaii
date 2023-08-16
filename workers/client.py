class Authorization:
    token: str = (
        "ODU5NTY5OTkwMDQxNDY4OTI4.GiEr5B.iRqdbIPG8YfJ3JW42q5k9AtFqwBTaWJUXoAxI4"
    )
    prefix: str = "!"
    owner_ids: list = [
        384076851494125569,
    ]


class Task:
    ...


class Emoji:
    """
    Default Buttons
    """

    bow: str = "<a:kawaiiBowPink:1141247541330063421>"
    ribbon: str = "<a:kawaiiPinkRibbon:1141247576390242375>"
    bunny: str = "<a:BunnyCarrots:1141247581465354272>"

    """
    Paginator Buttons
    """
    left: str = "<:left:1141353446742700123>"
    right: str = "<:right:1141353508394782730>"
    cancel: str = "<:cancel:1141353529873797120>"
    goto: str = "<:goto1:1141354412082741349>"
    goto2: str = "<:skipto:1141354608791396362>"
    teleport: str = "<:1_bearvamp:1141258271634759715>"
    delete: str = "<:ThinkingHmm:1141259209942507570>"


class Color:
    normal: int = 0xF4CCD4
    error: int = 0xF484F4
    warning: int = 0xF4ACAC
