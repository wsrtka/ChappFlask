from flask import Flask, request, abort, jsonify


app = Flask(__name__)


users = []


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


if __name__ == '__main__':
    app.run(debug=True)