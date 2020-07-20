from flask import Flask, request, abort


app = Flask(__name__)


users = []


@app.route('/')
def hello():
    return "Hello world"


@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']

    if username in users:
        abort(403)

    else:
        users.append(username)
        return 'Login successfull'


if __name__ == '__main__':
    app.run(debug=True)