from flask import Flask, jsonify
from datetime import datetime
from config import db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysql.30.svc.cluster.local:3306/userdb'  
db.init_app(app)

@app.route('/get_users', methods=['GET'])
def get_users():
    users = User.query.all()
    result = []
    for user in users:
        result.append({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'birth_date': user.birth_date.isoformat(),
            'family_relation': user.family_relation,
            'address': user.address
        })
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
