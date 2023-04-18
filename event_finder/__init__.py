import os

# Import Flask class from flask package with Blueprints
from flask import Flask, Blueprint
# Import SQLAlchemy class from flask_sqlalchemy package
from flask_sqlalchemy import SQLAlchemy

# Import the env.py file if it exists
if os.path.exists("env.py"):
    import env  # noqa

# Create an instance of the Flask Class
app = Flask(__name__)

# Create a SECRET_KEY key-value pair in app config.
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Create a SQLALCHEMY_TRACK_MODIFICATIONS key-value pair in app config.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Create a SQLALCHEMY_DATABASE_URI key-value pair in app config.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URI")

# Create an instance of the SQLAlchemy class
db = SQLAlchemy(app)


def create_flask_app():
    # Import the auth and event blueprints
    from event_finder.auth.routes import auth_routes
    from event_finder.event.routes import event_routes
    # Import the models
    from event_finder.event import models
    # Register the auth and event blueprints
    app.register_blueprint(auth_routes  )
    app.register_blueprint(event_routes)
    # Return the app
    return app
