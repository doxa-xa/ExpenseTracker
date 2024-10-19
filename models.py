from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    passwd_hash = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(120),nullable=False,unique=True)
    expenses = db.relationship('Expenses',backref='user', lazy=True)

class Expenses(db.Model):
    expense_id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(70))
    expense_type = db.Column(db.String(70))
    expense_name = db.Column(db.String(70))
    amount = db.Column(db.Float)
    date = db.Column(db.String(40))
    day_of_week = db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)

