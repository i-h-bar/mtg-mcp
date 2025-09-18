import os
from functools import lru_cache

import asyncpg


class Pool:
    __slots__ = ("_pool", "_connection")

    def __init__(self) -> None:
        self._pool = None
        self._connection = None

    async def connection(self) -> asyncpg.Connection:
        if not self._pool:
            self._pool = asyncpg.create_pool(os.getenv("PSQL_URI"))

        if self._connection is None:
            self._connection = await self._pool.__aenter__()

        return self._connection


@lru_cache(maxsize=1)
def get_pool() -> Pool:
    return Pool()
