from flask import Blueprint, render_template, request, redirect, session, flash, url_for, abort
from event_finder import db
from datetime import datetime
from event_finder.event.models import Event, User, Profile, Attendance

event = Blueprint("event", __name__, template_folder="../event_finder/templates")


@event.route("/")
def index():
    return render_template("base.html")


@event.route("/events")
def events():
    page = request.args.get('page', 1, type=int)
    current_date = datetime.utcnow().date()
    event_list = Event.query.filter(Event.date >= current_date).paginate(page=page, per_page=10)
    return render_template("events/events.html", events=event_list)


@event.route("/profile/<uuid>")
def profile(uuid):
    user = User.query.filter_by(uuid=uuid).first()
    user_profile = Profile.query.filter_by(user_uuid=user.uuid).first()
    if not user:
        abort(404)
    if user.uuid != session.get("user_uuid"):
        flash("You do not have permission to view this profile.")
        abort(403)
        return redirect("error/403.html")
    return render_template("profile.html", user=user, profile=user_profile)
