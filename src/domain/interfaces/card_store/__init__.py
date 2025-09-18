import abc


class RuleStore(abc.ABC):

    @abc.abstractmethod
    async def get_rule(self, rule: str) -> Rule: