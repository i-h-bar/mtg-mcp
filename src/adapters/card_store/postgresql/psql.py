import aiohttp
from dotenv import load_dotenv

from adapters.card_store.postgresql.queries import GET_CARD
from adapters.postgres.pool import get_pool
from domain.interfaces.card_store.interface import CardStore
from domain.models.card import Card

load_dotenv()


class PSQLCardStore(CardStore):
    __slots__ = ("pool",)

    def __init__(self) -> None:
        self.pool = get_pool()

    async def get(self, name: str) -> Card:
        conn = await self.pool.connection()
        result = dict(await conn.fetchrow(GET_CARD, name))

        async with aiohttp.ClientSession() as session:
            result["rulings"] = await (await session.get(result["front_rulings_url"])).json()

        return Card.model_validate(result)
