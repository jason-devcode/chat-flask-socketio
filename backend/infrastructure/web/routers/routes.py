from common.constants.http_methods import HttpEndpointMethods
from infrastructure.web.controllers.user import UserController

user_controller = UserController()

API_ENDPOINT_PREFIX = "/api/v1"


ROUTES = [
    # User endpoints
    {
        "path": f"{API_ENDPOINT_PREFIX}/user/read-user",
        "method": HttpEndpointMethods.GET.value,
        "handler": user_controller.read_user,
    },
]
