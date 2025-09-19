from uuid import UUID

from pydantic import BaseModel, Field


class Card(BaseModel):
    artist: str
    back_colour_identity: list[str] | None = Field(default=None)
    back_defence: str | None = Field(default=None)
    back_id: UUID | None = Field(default=None)
    back_illustration_id: UUID | None = Field(default=None)
    back_image_id: UUID | None = Field(default=None)
    back_keywords: list[str] | None = Field(default=None)
    back_loyalty: str | None = Field(default=None)
    back_mana_cost: str | None = Field(default=None)
    back_name: str | None = Field(default=None)
    back_oracle_text: str | None = Field(default=None)
    back_power: str | None = Field(default=None)
    back_scryfall_url: str | None = Field(default=None)
    back_toughness: str | None = Field(default=None)
    back_type_line: str | None = Field(default=None)
    front_colour_identity: list[str]
    front_defence: str | None = Field(default=None)
    front_id: UUID
    front_illustration_id: UUID
    front_image_id: UUID
    front_keywords: list[str]
    front_loyalty: str | None = Field(default=None)
    front_mana_cost: str
    front_name: str
    front_normalised_name: str
    front_oracle_text: str
    front_power: str | None = Field(default=None)
    front_rulings_url: str
    front_scryfall_url: str
    front_toughness: str | None = Field(default=None)
    front_type_line: str
    set_name: str
    sml: float
    rulings: dict
