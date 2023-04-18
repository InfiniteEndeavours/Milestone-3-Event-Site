import os

# Import Flask class from flask package with Blueprints
from flask import Flask, render_template
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


def fake_data():
    from event_finder.event.data.fake_data_generator import create_users, create_events, create_attendances
    # Create 10 users
    create_users(10)
    # Create 20 events
    create_events(20)
    # Create 30 attendances
    create_attendances(30)


@app.errorhandler(403)
def forbidden(e):
    return render_template("errors/403.html"), 404


@app.errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html"), 403


def create_flask_app():
    """
        Creates a Flask application object.

        This function creates a Flask application object, registers the auth and event blueprints,
        and imports the models used in the application.

        Returns:
            app (Flask): A Flask application object.
        """
    # Import the auth and event blueprints
    from event_finder.auth.routes import auth as auth_routes
    from event_finder.event.routes import event as event_routes
    # Import the models
    from event_finder.event import models
    # Register the auth and event blueprints
    app.register_blueprint(auth_routes)
    app.register_blueprint(event_routes)
    # Return the app
    return app
