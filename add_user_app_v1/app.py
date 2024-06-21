from flask import Flask, request, jsonify
from datetime import datetime
from config import db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysql.30.svc.cluster.local:3306/userdb'  
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    birth_date = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
    family_relation = data['family_relation']
    address = data['address']

    new_user = User(username=username, email=email, birth_date=birth_date, family_relation=family_relation, address=address)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)