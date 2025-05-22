from ..db_con import db

class Alert_rol(db.Model):
    __tablename__ = 'alert_rol'
    
    id = db.Column(db.Integer, primary_key=True)
    id_alert = db.Column(db.Numeric)
    id_rol = db.Column(db.Numeric)

    def to_dict(self):
        return {
            'id': self.id,
            'id_alert': self.id_alert,
            'id_rol': self.id_rol
        }