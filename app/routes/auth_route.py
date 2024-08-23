from flask import Blueprint, request, jsonify
from app.controllers import auth_controller

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['POST'])
def register():
    data = request.json
    response, status_code = auth_controller.register_user(data)
    return jsonify(response), status_code

@auth_blueprint.route('/login', methods=['POST'])
def login():
    data = request.json
    response, status_code = auth_controller.login_user(data)
    return jsonify(response), status_code
