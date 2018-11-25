

import jwt
from flask import Flask, jsonify, session

from database import db
from errors import http_error
from middlewares import auth, logger
from utils import config

app = Flask(__name__)
app.secret_key = 'secret-session-key'
app.wsgi_app = logger.LoggingMiddleware(app.wsgi_app)

conn = db.create_connection()

with conn:
    db.create_tables(conn)
    db.populate_with_test_members(conn)
    db.populate_with_test_users(conn)


# Routes


@app.route('/givemeatoken/<id>')
def get_token(id):
    with conn:
        users = db.select_users(conn)
        print(users)
        _users = list(filter(lambda user: user["id"] == int(id), users))

    if _users:
        return jwt.encode({'userId': _users.pop()["id"]},
                          config.JWT_AUTH['secret'],
                          config.JWT_AUTH['algorithm'])
    else:
        return not_found()


@app.route('/user')
@auth.require_api_token
def get_user():
    users = []
    _users = list(
        filter(lambda user: user['id'] == session['id'], users.users))

    if _users:
        return jsonify(_users.pop())
    else:
        return not_found()


@app.route('/members')
@auth.require_api_token
def get_members():
    try:
        with conn:
            members = db.select_members(conn)

        return jsonify(members)
    except TypeError as error:
        return internal_error(str(error))


@app.route('/members/<id>')
@auth.require_api_token
def get_member(id):
    with conn:
        member = db.select_member(conn, id)

    if member:
        return jsonify(member)

    else:
        return not_found()


@app.route('/members', methods=['POST'])
@auth.require_api_token
def add_member():
    return ""


@app.route('/members/<id>', methods=['PUT'])
@auth.require_api_token
def update_member():
    return ""

# Error handling


@app.errorhandler(401)
def unauthorized(error=None):
    return http_error.response(401, "Unauthorized")


@app.errorhandler(404)
def not_found(error=None):
    return http_error.response(404, "Not found")


@app.errorhandler(500)
def internal_error(error=None):
    return http_error.response(500, str(error))


if __name__ == "__main__":
    app.run()
