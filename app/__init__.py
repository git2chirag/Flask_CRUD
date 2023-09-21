from flask import Flask
from .db import mongo
from flask_caching import Cache
def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://mongo:27017/flaskapp"
    mongo.init_app(app)
    app.config['CACHE_TYPE'] = 'simple'
    cache=Cache(app)
    from .routes import user
    app.register_blueprint(user)

    return app
