from adapters.card_store.postgresql.psql import PSQL
from domain.interfaces.card_store.interface import CardStore


def initialise() -> CardStore:
    return PSQL()