from flask import Flask, render_template, request, redirect, url_for, jsonify
import requests

app = Flask(__name__)

# 서비스 상태를 나타내는 변수
service_ready = True

ADD_USER_SERVICE_URL = 'http://add.30.svc.cluster.local:80/add_user'
GET_USERS_SERVICE_URL = 'http://get.30.svc.cluster.local:80/get_users'
DELETE_USER_SERVICE_URL = 'http://delete.30.svc.cluster.local:80/delete_user'

@app.route('/')
def index():
    if service_ready:
        users = requests.get(GET_USERS_SERVICE_URL).json()
        return render_template('index.html', users=users)
    else:
        return "Service not ready", 503

@app.route('/add_user', methods=['POST'])
def add_user():
    if service_ready:
        user_data = {
            'username': request.form['username'],
            'email': request.form['email'],
            'birth_date': request.form['birth_date'],
            'family_relation': request.form['family_relation'],
            'address': request.form['address']
        }
        requests.post(ADD_USER_SERVICE_URL, json=user_data)
        return redirect(url_for('index'))
    else:
        return "Service not ready", 503

@app.route('/delete_user', methods=['POST'])
def delete_user():
    if service_ready:
        user_id = request.json.get('id')
        response = requests.post(DELETE_USER_SERVICE_URL, json={'id': user_id})
        if response.status_code == 200:
            return jsonify({"message": "User deleted successfully"}), 200
        else:
            return jsonify({"message": "User not found"}), 404
    else:
        return "Service not ready", 503

@app.route('/ready')
def ready():
    global service_ready
    if service_ready:
        return "OK", 200
    else:
        return "Not OK", 503

@app.route('/notready')
def notready():
    global service_ready
    service_ready = False
    return "Not OK", 503

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
