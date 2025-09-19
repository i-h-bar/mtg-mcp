from pydantic import BaseModel


class Definition(BaseModel):
    term: str
    definition: str
    rule_references: list[str]
