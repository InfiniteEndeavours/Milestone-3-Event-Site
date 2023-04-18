from flask import Blueprint, render_template

event = Blueprint("event", __name__, template_folder="../event_finder/templates")


@event.route("/")
def index():
    return render_template("base.html")


