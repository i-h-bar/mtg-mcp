from pydantic import BaseModel


class Rule(BaseModel):
    rule_number: str
    parent_rule: str
    subsection_id: int
    content: str
