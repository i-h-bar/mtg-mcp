from mcp.server.fastmcp import FastMCP
from adapters import card_store
from domain.models.card import Card

mcp = FastMCP("MTG")

card_store = card_store.initialise()

@mcp.resource("card://{name}")
async def get_card(name: str) -> Card:
    return await card_store.get(name)
