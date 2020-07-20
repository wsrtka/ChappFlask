from flask import Flask, request, abort, jsonify
from datetime import datetime
import uuid


app = Flask(__name__)


users = []
messages = dict()


@app.route('/')
def hello():
    return "Hello world"


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)

    if username in users or username is None:
        abort(403)

    else:
        users.append(username)
        return jsonify({
            'status': 'OK',
            'message': 'Successfully logged in',
        })


@app.route('/send', methods=['POST'])
def send():
    username = request.json.get('username', None)
    message = request.json.get('message', None)
    timestamp = datetime.now()
    id = uuid.uuid4()

    if username is None or username not in users:
        abort(401)

    if message is None or len(message) == 0:
        abort(400)

    messages[str(id)] = {
        'username': username,
        'message': message,
        'timestamp': timestamp,
        'id': id
    }

    return jsonify(messages)


if __name__ == '__main__':
    app.run(debug=True)