from asyncpg import (
    create_pool,
    RaiseError,
    PostgresError,
)


class Manager:
    def __init__(self: "Manager", *args, **kwargs) -> None:
        self.resolve: list = ()

    @classmethod
    async def create_task(
        self: "Manager",
        host: str,
        user: str,
        port: int,
        database: str,
        password: str,
    ) -> None:
        try:
            await create_pool(
                **{
                    "host": host,
                    "user": user,
                    "port": port,
                    "database": database,
                    "password": password,
                }
            )
        except Exception as e:
            raise Exception(
                f"DB Connection Error, Could not resolve connection to the database: {e}"
            )
