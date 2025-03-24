from typing import Callable, Dict, List

from fastapi import FastAPI
from pydantic import BaseModel


def register_routes_fastapi(app: FastAPI, routes: List[Dict[str, str]]):
    """
    Registers routes dynamically in a FastAPI application.

    This function takes a list of route definitions and registers them in a FastAPI instance.
    Each route should be defined as a dictionary containing:
        - "path" (str): The endpoint path (e.g., "/register").
        - "method" (str): The HTTP method (e.g., "POST").
        - "handler" (Callable): The function that processes the request.

    Args:
        app (FastAPI): The FastAPI application instance.
        routes (List[Dict[str, str]]): A list of route dictionaries to register.

    Example:
        routes = [
            {"path": "/register", "method": "POST", "handler": user_controller.register}
        ]
        register_routes_fastapi(app, routes)
    """
    for route in routes:
        # Dynamically create a Pydantic model for request validation
        request_model = type("RequestModel", (BaseModel,), {"__annotations__": {}})

        async def handler(data: request_model):
            response, status_code = route["handler"](**data.dict())
            return response

        app.add_api_route(route["path"], handler, methods=[route["method"]])
