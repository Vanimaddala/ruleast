# database.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(50), nullable=False)
    income = db.Column(db.Float, nullable=False)
    spend = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

def init_db(app):
    with app.app_context():
        db.create_all()
