from adapters.rule_store.postgresql.psql import PSQLRuleStore
from domain.interfaces.rule_store.interface import RuleStore


def initialise() -> RuleStore:
    return PSQLRuleStore()
