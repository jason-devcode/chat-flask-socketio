from flask import Flask
from flask_socketio import SocketIO
from infrastructure.web.adapters.flask import register_routes_flask
from infrastructure.web.routers.routes import ROUTES

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "123456789"
    socketio.init_app(app)

    # register all routes
    register_routes_flask(app, ROUTES)

    return app
