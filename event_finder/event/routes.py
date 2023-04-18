from flask import Blueprint, render_template

event_routes = Blueprint("event", __name__, template_folder="../event_finder/templates")

@event_routes.route("/")
def index():
    return render_template("base.html")


