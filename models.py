from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    department = db.Column(db.String(50))
    income = db.Column(db.Float)
    spend = db.Column(db.Float)

# Rule Node model for AST
class RuleNode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20))  # 'operator' or 'operand'
    value = db.Column(db.String(100), nullable=True)
    left_id = db.Column(db.Integer, db.ForeignKey('rule_node.id'), nullable=True)
    right_id = db.Column(db.Integer, db.ForeignKey('rule_node.id'), nullable=True)

    left = db.relationship('RuleNode', remote_side=[id], foreign_keys=[left_id])
    right = db.relationship('RuleNode', remote_side=[id], foreign_keys=[right_id])
