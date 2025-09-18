from pydantic import BaseModel


class Rule(BaseModel):
    rule_number: str
    parent_rule: str
    section_number: int
    section_title: str
    subsection_number: int
    subsection_title: str
    content: str
