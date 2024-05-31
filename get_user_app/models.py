from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    family_relation = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(255), nullable=False)