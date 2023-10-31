from pydantic import Field
from project.routes.v1.example.dtos.base_dto import BaseDto


class FooRequest(BaseDto):

    name: str = Field(
        alias = "name",
        description = "name of the user",
        example = "John doe",
        title = "Name"
    )
