from ..db_con import db

class Readings(db.Model):
    __tablename__ = 'readings_raw'
    
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Numeric)
    time = db.Column(db.DateTime)
    sensor = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'level': self.level,
            'sensor': self.sensor,
            'time': self.time
        }
