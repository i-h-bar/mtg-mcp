from mcp.server.fastmcp import FastMCP
from adapters import card_store, rule_store
from domain.models.card import Card
from domain.models.rule import Rule


card_store = card_store.initialise()
rule_store = rule_store.initialise()


mcp = FastMCP("MTG")


@mcp.tool()
async def get_card(name: str) -> Card:
    return await card_store.get(name)

@mcp.tool()
async def get_rule(rule_number: str) -> Rule:
    return await rule_store.get_rule(rule_number)

@mcp.tool()
async def get_subsection(subsection_number: int) -> list[Rule]:
    return await rule_store.get_subsection(subsection_number)

@mcp.tool()
async def get_section(section_number: int) -> list[Rule]:
    return await rule_store.get_section(section_number)

if __name__ == "__main__":
    mcp.run(transport="sse")