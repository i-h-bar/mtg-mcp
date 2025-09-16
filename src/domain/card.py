from domain.models.card import Card


async def get_card(name: str) -> Card:
    return