from .db import mongo
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

def save_user(data):
    hashed_password = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    user = {"name": data["name"], "email": data["email"], "password": hashed_password}
    return mongo.db.users.insert_one(user)

def get_all_users():
    users = list(mongo.db.users.find({}))
    for user in users:
        user["_id"] = str(user["_id"])
    return users

def get_user_by_id(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    if user:
        user["_id"] = str(user["_id"])
    return user

def update_user(user_id, data):
    if "password" in data:
        data["password"] = bcrypt.generate_password_hash(data["password"]).decode('utf-8')
    return mongo.db.users.update_one({"_id": user_id}, {"$set": data})

def delete_user(user_id):
    return mongo.db.users.delete_one({"_id": user_id})
