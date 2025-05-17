from ..db_con import db

class Sensors(db.Model):
    __tablename__ = 'sensors'
    
    id = db.Column(db.String(50), primary_key=True)
    coord = db.Column(db.String(150))
    state = db.Column(db.String(50))