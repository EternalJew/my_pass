from api import db
from datetime import datetime


class IT_College_members(db.Model):
    __tablename__ = 'it_college_members'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    unique_code = db.Column(db.String(40), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('it_college_type.id'), nullable=False)
    type = db.relationship('IT_College_Type')
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, first_name, last_name, email,  unique_code, type_id):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.unique_code = unique_code
        self.type_id = type_id