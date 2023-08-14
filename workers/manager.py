from asyncpg import (
    create_pool,
    RaiseError,
    PostgresError,
)


class Manager:
    def __init__(
        self: "Manager",
        host: str,
        user: str,
        port: int,
        database: str,
        password: str,
    ) -> None:
        self.host: str = host
        self.user: str = user
        self.port: str = port
        self.database: str = database
        self.password: str = password

    @classmethod
    async def create_task(self: "Manager") -> None:
        try:
            await create_pool(
                **{
                    "host": self.host,
                    "user": self.user,
                    "port": self.port,
                    "database": self.database,
                    "password": self.password,
                }
            )
        except:
            raise Exception(
                "DB Connection Error, Could not resolve connection to the database"
            )
