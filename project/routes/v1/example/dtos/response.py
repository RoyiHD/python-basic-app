from pydantic import Field
from project.routes.v1.example.dtos.base_dto import BaseDto


class FooResponse(BaseDto):
    
    message: str = Field(
        alias = "message",
        description = "response message",
        example = "Successful request and response validation",
        title = "Message"
    )
