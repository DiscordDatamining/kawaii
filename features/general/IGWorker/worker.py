import json
import requests
from requests import (
    get,
    post,
    request,
    ConnectionError,
    JSONDecodeError,
)


class Worker:
    def __init__(self: "Worker", *args, **kwargs) -> None:
        self.config = json.load(
            open(
                file="api.json ",
                encoding="UTF-8",
            )
        )

    async def add_follow_task(
        self: "Worker", username: str = None, *args, **kwargs
    ) -> None:
        if not username:
            return 0
        data = get(url="")
