from flask import Blueprint, jsonify
from utils.auth import check_permission  # Custom decorator

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route('/admin', methods=['GET'])
@check_permission('admin')  # Admin check
def admin_dashboard():
    return jsonify({'message': 'Admin dashboard'})
