from dotenv import load_dotenv

from adapters.postgres.pool import get_pool
from adapters.rule_store.postgresql.queries import GET_RULE, GET_SECTION, GET_SUBSECTION
from domain.interfaces.rule_store.interface import RuleStore
from domain.models.rule import Rule

load_dotenv()


class PSQLRuleStore(RuleStore):
    __slots__ = ("pool",)

    def __init__(self) -> None:
        self.pool = get_pool()

    async def get_rule(self, rule: str) -> Rule:
        conn = await self.pool.connection()
        result = dict(await conn.fetchrow(GET_RULE, rule))

        return Rule.model_validate(result)

    async def get_section(self, section_number: int) -> list[Rule]:
        conn = await self.pool.connection()
        return [Rule.model_validate(dict(result)) for result in await conn.fetch(GET_SECTION, section_number)]

    async def get_subsection(self, subsection: int) -> list[Rule]:#
        conn = await self.pool.connection()
        return [Rule.model_validate(dict(result)) for result in await conn.fetch(GET_SUBSECTION, subsection)]

if __name__ == "__main__":
    import asyncio
    async def main():
        store = PSQLRuleStore()
        rule = await store.get_subsection(202)
        print(rule)

    asyncio.run(main())