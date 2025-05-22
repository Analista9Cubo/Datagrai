from ..db_con import db

class Alert(db.Model):
    __tablename__ = 'alert_rules'
    
    id = db.Column(db.Integer, primary_key=True)
    alert_level = db.Column(db.String(50))
    id_sensor = db.Column(db.String(50))
    umb_min = db.Column(db.Numeric)
    umb_max = db.Column(db.Numeric)

    def to_dict(self):
        return {
            'id': self.id,
            'alert_level': self.alert_level,
            'id_sensor': self.id_sensor,
            'umb_min': self.umb_min,
            'umb_max': self.umb_max
        }