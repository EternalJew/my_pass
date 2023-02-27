from api import db, app
from datetime import datetime

class Students(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    student_unique_code = db.Column(db.String(40), unique=True, nullable=False)
    registered = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, first_name, last_name, email,  student_unique_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.student_unique_code = student_unique_code