from common.constants.http_methods import HttpEndpointMethods
from common.constants.roles import RoleBitPosition
from common.utils.logger import Logger
from domain.ports.repositories.user import UserRepository
from domain.use_cases.auth.signup import SignUpUseCase
from infrastructure.web.controllers.auth import AuthenticationController
from infrastructure.web.controllers.user import UserController

user_controller = UserController()

# logger = Logger()
# user_repository = UserRepository()
# signup_use_case = SignUpUseCase(logger=logger, user_repository=user_repository)
# auth_controller = AuthenticationController(
#     logger=Logger(),
# )

API_ENDPOINT_PREFIX = "/api/v1"

ROUTES = [
    # Authentication User
    # {
    #     "path": f"{API_ENDPOINT_PREFIX}/auth/signup",
    #     "method": HttpEndpointMethods.POST.value,
    #     "handler": auth_controller.signup,
    #     "protect": False,  # by default this is True
    #     "description": "",
    # },
    # User endpoints
    {
        "path": f"{API_ENDPOINT_PREFIX}/user/read-user",
        "method": HttpEndpointMethods.GET.value,
        "handler": user_controller.read_user,
        "roles": [RoleBitPosition.USER],
        "protect": True,  # by default this is True
        "description": "",
    },
]
