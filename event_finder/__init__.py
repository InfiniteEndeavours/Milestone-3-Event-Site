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


@app.errorhandler(403)
def forbidden(e):
    """
    Route returns the 403 page.

    :param e:
    :return: 403.html
    """
    return render_template("errors/403.html"), 404


@app.errorhandler(404)
def page_not_found(e):
    """
    Route returns the 404 page.

    :param e:
    :return: 404.html
    """
    return render_template("errors/404.html"), 403


def create_flask_app():
    """
    Create a Flask application object.

    This function is used to create a Flask application object and
    register the blueprints.

    Returns:
        app (Flask): Flask application object
    """
    from event_finder.auth.routes import auth as auth_routes
    from event_finder.event.routes import event as event_routes
    from event_finder.admin.routes import admin as admin_routes
    # Import the models
    from event_finder.event import models
    app.register_blueprint(auth_routes)
    app.register_blueprint(admin_routes)
    app.register_blueprint(event_routes)
    # Return the app
    return app
