import os

import aiohttp
import asyncpg
from dotenv import load_dotenv

from adapters.card_store.postgresql.queries import GET_CARD
from domain.interfaces.card_store.interface import CardStore
from domain.models.card import Card

load_dotenv()


class PSQL(CardStore):
    __slots__ = ("_pool",)

    def __init__(self) -> None:
        self._pool = None

    async def pool(self) -> asyncpg.Pool:
        if self._pool is None:
            self._pool =  asyncpg.create_pool(os.getenv("PSQL_URI"))

        return self._pool

    async def get(self, name: str) -> Card:
        pool = await self.pool()

        async with pool as conn:
            result = dict(await conn.fetchrow(GET_CARD, name))

        async with aiohttp.ClientSession() as session:
            result["rulings"] = await (await session.get(result["front_rulings_url"])).json()

        return Card.model_validate(result)
