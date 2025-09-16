import abc

from domain.models.card import Card


class CardStore(abc.ABC):
    @abc.abstractmethod
    async def get(self, name: str) -> Card:
        raise NotImplementedError