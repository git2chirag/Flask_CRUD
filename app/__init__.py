from flask import Flask
from .db import mongo

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongo:27017/flaskapp"
    mongo.init_app(app)

    from .routes import user
    app.register_blueprint(user)

    return app
