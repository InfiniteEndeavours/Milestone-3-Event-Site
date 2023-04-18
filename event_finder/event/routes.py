from flask import Blueprint

event_routes = Blueprint("event", __name__, template_folder="../event_finder/templates")

@event_routes.route("/")
def index():
    return "Hello World"


