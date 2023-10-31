from pydantic import BaseModel


class BaseDto(BaseModel):

    class Config:
        extra = "forbid"
