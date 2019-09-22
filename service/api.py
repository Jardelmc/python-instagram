from flask import Flask, jsonify, request

from login import loginService
from get_users_from_node import get_users_from_hashtags, get_users
from follow import followDialy
from unfollow import unfollowDialy

app = Flask(__name__)

loggedProfiles = {}


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    return jsonify({'message': 'ok'}), 200


if __name__ == '__main__':
    app.run(debug=True)
