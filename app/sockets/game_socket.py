from flask_socketio import join_room, emit
from flask_login import current_user
from ..services.game_logic import process_shot

def register_sockets(socketio):
    @socketio.on("join_game")
    def join(data):
        join_room(data["game_id"])
    @socketio.on("fire_shot")
    def fire(data):
        hit = process_shot(data["game"], current_user, data["row"], data["col"])
        emit(
            "shot_result", 
            {"row":data["row"],"col":data["col"], "hit":hit},
            room=data["game_id"])