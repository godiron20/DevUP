from pydantic import BaseModel, Field, ConfigDict, UUID4

from src.conts.users import user_position, tren_group


class UsersDB(BaseModel):
    id: int = Field(description="айди пользователя")
    username: str = Field(description="имя пользователя")
    lang: str = Field(description="язык")
    calories: float | None = Field(description="калории", default=None)
    position: user_position | None = Field(description="позиция", default=None)



class TrenDB(BaseModel):
    id: int = Field(description="Position")
    group: tren_group = Field(description="группа мышц")
    colvo_pod: str = Field(description="количество подходов")
    colvo_pov: str = Field(description="количество повторений")

class TrenFilter(BaseModel):
    limit: int = Field(default=-1)
    offset: int = Field(default=0)
    group: tren_group | None = Field(description="группа мышц")
    colvo_pod_from: int | None = Field(description="кол-во подходов от")
    colvo_pod_to: int | None = Field(description="кол-во подходов до")
    colvo_pov_from: int | None = Field(description="кол-во повторений от")
    colvo_pov_to: int | None = Field(description="кол-во повторений до")



class RacionDB(BaseModel):
    id: int = Field(description="Position")
    name: str = Field(description="Имя")
    vid: str = Field(description="Вид")
    calories: float = Field(description="Количество калорий")
    ygli: float = Field(description="Углеводы")
    fats: float = Field(description="Жиры")
    belki: float = Field(description="Белки")