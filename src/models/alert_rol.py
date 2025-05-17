from ..db_con import db

class Alert_rol(db.Model):
    __tablename__ = 'alert_rol'
    
    id = db.Column(db.Integer, primary_key=True)
    id_alert = db.Column(db.Numeric)
    id_rol = db.Column(db.Numeric)