from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_login import LoginManager

deb=SQLAlchemy()
socketio = SocketIO()
login_manager = LoginManager()