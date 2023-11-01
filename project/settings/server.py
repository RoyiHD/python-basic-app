"""
Module to manage environment variables
"""
from pydantic import Field
from pydantic_settings import BaseSettings


class ServerSettings(BaseSettings):
    
    host: str = Field(
        alias = "host",
        description = "server host",
        example = "0.0.0.0",
        title = "Host"
    )

    port: int = Field(
        alias = "port",
        description = "server port",
        example = 3000,
        title = "Port"
    )

    class Config:
        env_prefix = "SERVER_"
