from flask import Blueprint, jsonify, request
from .models import save_user, get_all_users, get_user_by_id, update_user, delete_user
from bson.objectid import ObjectId

user = Blueprint('user', __name__)

@user.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    user_id = save_user(data)
    return jsonify({"id": str(user_id.inserted_id)}), 201

@user.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users), 200

@user.route('/users/<user_id>', methods=['GET'])
def get_single_user(user_id):
    user = get_user_by_id(ObjectId(user_id))
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user), 200

@user.route('/users/<user_id>', methods=['PUT'])
def update_single_user(user_id):
    data = request.get_json()
    result = update_user(ObjectId(user_id), data)
    if result.modified_count == 0:
        return jsonify({"error": "User not found or data unchanged"}), 404
    return jsonify({"message": "User updated successfully"}), 200

@user.route('/users/<user_id>', methods=['DELETE'])
def delete_single_user(user_id):
    result = delete_user(ObjectId(user_id))
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted successfully"}), 200
