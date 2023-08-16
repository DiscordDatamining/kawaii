from asyncpg import (
    create_pool,
    RaiseError,
    PostgresError,
)


class Manager:
    def __init__(self: "Manager", *args, **kwargs) -> None:
        self.resolve: list = ()
