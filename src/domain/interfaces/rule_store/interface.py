import abc

from domain.models.rule import Rule


class RuleStore(abc.ABC):

    @abc.abstractmethod
    async def get_rule(self, rule: str) -> Rule:
        raise NotImplementedError
