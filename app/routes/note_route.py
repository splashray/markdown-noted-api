from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.controllers import note_controller

note_blueprint = Blueprint('note', __name__)

@note_blueprint.route('/create', methods=['POST'])
@jwt_required()
def create_note():
    user_id = get_jwt_identity()
    data = request.json
    response, status_code = note_controller.create_note_for_user(user_id, data)
    return jsonify(response), status_code

@note_blueprint.route('/getall/user', methods=['GET'])
@jwt_required()
def get_notes_for_user():
    user_id = get_jwt_identity()
    response, status_code = note_controller.get_notes_for_user(user_id)
    return jsonify(response), status_code

@note_blueprint.route('/getone/user/<int:note_id>', methods=['GET'])
@jwt_required()
def get_note_for_user(note_id):
    user_id = get_jwt_identity()
    response, status_code = note_controller.get_note_for_user(user_id, note_id)
    return jsonify(response), status_code

@note_blueprint.route('/update/<int:note_id>', methods=['PUT'])
@jwt_required()
def update_note_for_user(note_id):
    user_id = get_jwt_identity() 
    data = request.json
    response, status_code = note_controller.update_note_for_user(user_id, note_id, data)
    return jsonify(response), status_code

@note_blueprint.route('/delete/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note_for_user(note_id):
    user_id = get_jwt_identity()  
    response, status_code = note_controller.delete_note_for_user(user_id, note_id)
    return jsonify(response), status_code
