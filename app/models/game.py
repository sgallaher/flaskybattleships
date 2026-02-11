from ..extensions import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(8), unique=True)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    opponent_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    status = db.Column(db.String(20), default="waiting")
    turn_player_id=db.Column(db.Integer)