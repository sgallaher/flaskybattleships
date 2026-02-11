from ..models.shot import Shot
from ..models.ship import Ship
from ..extensions import db
def process_shot(game, player, row, col):
    ships = Ship.query.filter_by(game_id=game.id).all()
    
    hit = False 
    for ship in ships:
        if ship.player_id == player.id:
            continue
        if ship.contains(row,col):
            hit = True
            break
    shot = Shot(game_id=game.id, player_id=player.id, row=row, col=col, hit=hit)
    db.session.add(shot)
    db.session.commit()


