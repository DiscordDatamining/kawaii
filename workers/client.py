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
    teleport: str = "<:1_bearvamp:1141258271634759715>"
    delete: str = "<:ThinkingHmm:1141259209942507570>"


class Color:
    normal: int = 0xF4CCD4
    error: int = 0xF484F4
    warning: int = 0xF4ACAC
