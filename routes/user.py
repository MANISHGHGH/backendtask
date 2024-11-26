from flask import Blueprint, jsonify

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/user', methods=['GET'])
def user_dashboard():
    return jsonify({'message': 'User dashboard'})
