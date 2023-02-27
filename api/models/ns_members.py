from api import db, app
from datetime import datetime

class NS_members(db.Model):
    __tablename__ = 'ns_members'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    ns_unique_code = db.Column(db.String(40), unique=True, nullable=False)
    type_id = db.Column(db.Integer, db.ForeignKey('ns_members_type.id'), nullable=False)
    type = db.relationship('NS_Members_Type')
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, first_name, last_name, email,  ns_unique_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.ns_unique_code = ns_unique_code