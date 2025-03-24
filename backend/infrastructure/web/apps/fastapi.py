from fastapi import FastAPI
from infrastructure.web.adapters.fastapi import register_routes_fastapi
from infrastructure.web.routers.routes import ROUTES


def create_app():

    app = FastAPI()
    # register all routes
    register_routes_fastapi(app, ROUTES)

    return app
