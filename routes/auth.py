from flask import Blueprint, request, jsonify
from utils.hash import hash_password, check_password
from utils.jwt import encode_auth_token

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role')
    
    hashed_password = hash_password(password)
    # Add user to database (assuming db session available)
    
    return jsonify({'message': 'User registered successfully!'}), 201
