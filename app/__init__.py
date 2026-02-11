from flask import Flask
from .extensions import db, socketio, login_manager

def create_app():
    app= Flask(__name__)
    app.config.from_object("config.Congig")

    db.init_app(app)
    socketio.init_app(app, cors_allowed_origins="*")
    login_manager.init_app(app)

    from .routes.auth import auth_bp
    from .routes.games import game_bp
    from .sockets.game_socket import register_sockets

    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)

    register_sockets(socketio)

    return app

