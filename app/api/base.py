from typing import Callable
from fastapi.routing import APIRoute


class BaseRoute(APIRoute):
    def __init__(self, path: str, endpoint: Callable, **kwargs):
        del kwargs['response_model_exclude_none']
        super().__init__(path, endpoint, response_model_exclude_none=True, **kwargs)
