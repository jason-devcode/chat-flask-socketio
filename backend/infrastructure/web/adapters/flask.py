from functools import wraps
from typing import Callable, Dict, List

from common.constants.roles import RoleBitPosition
from common.utils.roles import has_roles_in_bitmask
from flask import Flask
from flask import g as global_attr
from flask import jsonify, request
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request


def register_routes_flask(app: Flask, routes: List[Dict[str, Callable]]):
    """
    Registers routes dynamically in a Flask application, supporting JWT authentication
    and role-based access control with bitmasks.

    Each route can specify:
        - Required roles for access (bitmask-based).
        - Whether authentication is needed (protect=True by default).

    Args:
        app (Flask): The Flask instance.
        routes (List[Dict[str, Callable]]): Route definitions.
    """
    for route in routes:
        app.route(route["path"], methods=[route["method"]])(_apply_middleware(route))


def _apply_middleware(route: Dict[str, Callable]) -> Callable:
    """
    Applies JWT authentication and role-based access control if required.

    Args:
        route (Dict[str, Callable]): The route definition.

    Returns:
        Callable: The wrapped function with middleware applied.
    """
    protect = route.get("protect", True)
    allowed_roles = route.get("roles", [])

    handler = lambda: _process_request(route["handler"])

    return _jwt_and_role_middleware(handler, allowed_roles, protect)


def _process_request(handler: Callable):
    """
    Extracts request data and calls the controller method with user information.

    Args:
        handler (Callable): The controller method to execute.

    Returns:
        Response: The Flask JSON response.
    """
    data = request.form.to_dict()
    file = request.files.get("file")

    response, status_code = (
        handler(
            file,
            **data,
            user_id=global_attr.user["id"],
            role_bitmask=global_attr.user["role_bitmask"]
        )
        if file
        else handler(
            **data,
            user_id=global_attr.user["id"],
            role_bitmask=global_attr.user["role_bitmask"]
        )
    )
    return jsonify(response), status_code


def _jwt_and_role_middleware(
    handler: Callable, allowed_roles: List[RoleBitPosition], protect: bool
):
    """
    Middleware that applies JWT authentication and role-based access control.

    Args:
        handler (Callable): The function to wrap.
        allowed_roles (List[RoleBitPosition]): List of roles required for access.
        protect (bool): If True, applies authentication and authorization.

    Returns:
        Callable: The wrapped function.
    """

    @wraps(handler)
    def decorated_function(*args, **kwargs):
        try:
            if protect:
                result, json, status = _authenticate_user()
                if not result:
                    return json, status
                if allowed_roles and not _check_user_roles(allowed_roles):
                    return (
                        jsonify(
                            {
                                "error": "Forbidden",
                                "message": "Insufficient permissions",
                            }
                        ),
                        403,
                    )
            else:
                global_attr.user = {"id": None, "role_bitmask": 0}

            return handler(*args, **kwargs)
        except Exception as unknown_error:
            return (
                jsonify(
                    {
                        "error": str(unknown_error),
                        "message": "Cannot perform this request",
                    }
                ),
                403,
            )

    return decorated_function


def _authenticate_user():
    """
    Verifies the JWT and extracts user identity, storing it in `global_attr`.
    """
    try:
        verify_jwt_in_request()
        user_data = get_jwt_identity()
        global_attr.setdefault(
            "user", {"id": user_data["id"], "role_bitmask": user_data["role_bitmask"]}
        )
        return True, None, None
    except Exception as e:
        return False, jsonify({"error": "Unauthorized", "message": str(e)}), 401


def _check_user_roles(allowed_roles: List[RoleBitPosition]) -> bool:
    """
    Checks if the user has the required roles.

    Args:
        allowed_roles (List[RoleBitPosition]): Required roles.

    Returns:
        bool: True if user has the required roles, False otherwise.
    """

    return has_roles_in_bitmask(
        global_attr.get("user", {"role_bitmask": 0})["role_bitmask"], allowed_roles
    )
