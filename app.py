# app.py

from flask import Flask, request, jsonify, render_template
from database import db, init_db, User
from rules import create_rule, evaluate_rule

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///c:/sqlite-dll-win-x86-3460100/rules.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
init_db(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(
        name=data['name'],
        age=data['age'],
        department=data['department'],
        income=data['income'],
        spend=data['spend']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully!'}), 201

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.json
    rule_string = data['rule']
    user_data = {
        "age": data['age'],
        "department": data['department'],
        "income": data['income'],
        "spend": data['spend']
    }
    ast = create_rule(rule_string)
    result = evaluate_rule(ast, user_data)
    return jsonify({'eligible': result})

if __name__ == '__main__':
    app.run(debug=True)
