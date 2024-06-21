from flask import Flask, request, jsonify
from datetime import datetime
from config import db
from models import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@mysql.30.svc.cluster.local:3306/userdb'  
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = request.json.get('id')
    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted successfully"}), 200
    else:
        return jsonify({"message": "User not found"}), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)