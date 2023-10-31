from functools import wraps
from flask import g, jsonify, Response
from typing import Callable

from pydantic import BaseModel

def response_dto(dto_cls: type[BaseModel]) -> Callable:

    def decorator(route: Callable) -> Callable:

        @wraps(route)
        def wrapper(*args, **kwargs) -> Response:
            raw_response = route(*args, **kwargs)

            response_dto = g.response_dto = dto_cls.model_validate(raw_response)
            response = jsonify(response_dto.model_dump(by_alias=True))
            response.status_code = 200

            return response

        return wrapper

    return decorator
