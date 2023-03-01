from api import db, app
from datetime import datetime


class Main_Type(db.Model):
    __tablename__ = 'main_type'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name):
        self.name = name