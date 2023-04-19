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


@event.route("/events/create_event", methods=["GET", "POST"])
def create_event():
    user = User.query.filter_by(uuid=session.get("user_uuid")).first()
    if not user:
        flash("You must be logged in to create an event.")
        abort(403)
        return redirect("error/403.html")

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        location = request.form.get("location")
        date = request.form.get("date")
        start_time = request.form.get("start_time")
        end_time = request.form.get("end_time")

        # Check if all fields are filled out
        event_fields = [title, description, location, date, start_time, end_time]
        for field in event_fields:
            if not field:
                flash(f"Please fill out the required fields.")
                return render_template("events/create_event.html")
        new_event = Event(title=title, description=description, location=location, date=date,
                          start_time=start_time, end_time=end_time, creator_id=user.uuid)
        db.session.add(new_event)
        db.session.commit()
        flash("Event created successfully.")
        return redirect(url_for("event.events"))

    return render_template("events/create_event.html")


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
