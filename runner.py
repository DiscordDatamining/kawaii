import os
from modules.margiela import Margiela
from workers.client import Authorization

os.environ.update(
    {
        "JISHAKU_HIDE": "True",
        "JISHAKU_RETAIN": "True",
        "JISHAKU_NO_UNDERSCORE": "True",
        "JISHAKU_NO_AUTO_FOOTER": "True",
        "JISHAKU_NO_UNDERSCORE_NUMBER": "True",
        "JISHAKU_SHELL_NO_DM_TRACEBACK": "True",
    }
)
Client = Margiela()

if __name__:
    Client.run(
        token=Authorization.token,
        reconnect=True,
    )
