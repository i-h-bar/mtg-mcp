import abc

from domain.models.definition import Definition
from domain.models.rule import Rule


class RuleStore(abc.ABC):

    @abc.abstractmethod
    async def get_rule(self, rule: str) -> Rule | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_section(self, section: int, limit: int, offset: int) -> list[Rule] | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_subsection(self, subsection: int) -> list[Rule] | None:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_definition(self, term: str) -> Definition | None:
        raise NotImplementedError
