from typing import Callable, Dict, List

from flask import Flask, jsonify, request


def register_routes_flask(app: Flask, routes: List[Dict[str, Callable]]):
    """
    Dynamically registers routes in a Flask application, including support for file uploads.

    This function takes a list of route definitions and registers them as Flask routes.
    Each route should be defined as a dictionary containing:
        - "path" (str): The endpoint path (e.g., "/upload").
        - "method" (str): The HTTP method (e.g., "POST").
        - "handler" (Callable): The function that processes the request.

    If the request includes a file, it is extracted from `request.files` and passed to the handler function.
    Other form data is extracted from `request.form.to_dict()`.

    Args:
        app (Flask): The Flask application instance.
        routes (List[Dict[str, Callable]]): A list of route dictionaries to register.

    Example:
        routes = [
            {"path": "/upload", "method": "POST", "handler": user_controller.upload_profile_picture}
        ]
        register_routes_flask(app, routes)
    """
    for route in routes:

        def handler():
            data = request.form.to_dict()  # Extract form data
            file = request.files.get("file")  # Get uploaded file (if exists)

            # Call the controller method with or without the file
            response, status_code = (
                route["handler"](file, **data) if file else route["handler"](**data)
            )
            return jsonify(response), status_code

        app.route(route["path"], methods=[route["method"]])(handler)
