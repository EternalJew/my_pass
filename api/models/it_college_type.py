from api import db, app
from datetime import datetime


class IT_College_Type(db.Model):
    __tablename__ = 'it_college_type'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name):
        self.name = name