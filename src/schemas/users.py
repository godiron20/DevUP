from pydantic import BaseModel, Field, ConfigDict, UUID4

from conts.users import user_position


class UsersDB(BaseModel):
    id: int = Field(description="Position", default=None)
    name: str = Field(description="Position", default=None)
    lang: str = Field(description="Position", default=None)
    calories: float | None = Field(description="Position", default=None)
    position: user_position | None = Field(description="Position", default=None)
