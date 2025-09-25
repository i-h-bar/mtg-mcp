from dotenv import load_dotenv

from adapters.postgres.pool import get_pool
from adapters.rule_store.postgresql.queries import GET_DEFINITION, GET_RULE, GET_SECTION, GET_SUBSECTION
from domain.interfaces.rule_store.interface import RuleStore
from domain.models.definition import Definition
from domain.models.rule import Rule

load_dotenv()


class PSQLRuleStore(RuleStore):
    __slots__ = ("pool",)

    def __init__(self) -> None:
        self.pool = get_pool()

    async def get_rule(self, rule: str) -> Rule | None:
        conn = await self.pool.connection()

        if result := await conn.fetchrow(GET_RULE, rule):
            return Rule.model_validate(dict(result))

        return None

    async def get_section(self, section_number: int) -> list[Rule] | None:
        conn = await self.pool.connection()

        if results := await conn.fetch(GET_SECTION, section_number):
            return [Rule.model_validate(dict(result)) for result in results]

        return None

    async def get_subsection(self, subsection: int) -> list[Rule] | None:
        conn = await self.pool.connection()

        if results := await conn.fetch(GET_SUBSECTION, subsection):
            return [Rule.model_validate(dict(result)) for result in results]

        return None

    async def get_definition(self, term: str) -> Definition | None:
        conn = await self.pool.connection()

        if result := await conn.fetchrow(GET_DEFINITION, term):
            return Definition.model_validate(dict(result))

        return None
