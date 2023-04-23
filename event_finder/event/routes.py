from flask import Blueprint, render_template, request, redirect, session, flash, url_for, abort
from event_finder import db
from datetime import datetime
from event_finder.event.models import Event, User, Profile, Attendance
from event_finder.event.helpers import db_find_first
import random

event = Blueprint("event", __name__, template_folder="../event_finder/templates")


@event.route("/")
def index():
    current_events = list(Event.query.filter(Event.date >= datetime.utcnow()).all())
    if current_events:
        event_one = current_events[random.randint(0, len(current_events) - 1)]
        event_two = current_events[random.randint(0, len(current_events) - 1)]
        return render_template("index.html", event_one=event_one, event_two=event_two)
    return render_template("index.html")



@event.route("/events")
def events():
    page = request.args.get('page', 1, type=int)
    current_date = datetime.utcnow().date()
    event_list = Event.query.filter(Event.date >= current_date).order_by(Event.id).paginate(page=page, per_page=10)
    return render_template("events/events.html", events=event_list)


@event.route("/events/<int:event_id>")
def event_info(event_id):
    event_data = db_find_first(Event, id=event_id)
    if not event_data:
        abort(404)
    return render_template("events/event_info.html", event=event_data)


@event.route("/events/create_event", methods=["GET", "POST"])
def create_event():
    user = db_find_first(User, uuid=session.get("user_uuid"))
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


@event.route("/events/<int:event_id>/edit_event", methods=["GET", "POST"])
def edit_event(event_id):
    event_to_edit = db_find_first(Event, id=event_id)
    event_date = event_to_edit.date.strftime("%Y-%m-%d")
    if request.method == "POST":
        event_to_edit.title = request.form.get("title")
        event_to_edit.description = request.form.get("description")
        event_to_edit.location = request.form.get("location")
        event_to_edit.date = request.form.get("date")
        event_to_edit.start_time = request.form.get("start_time")
        event_to_edit.end_time = request.form.get("end_time")
        db.session.add(event_to_edit)
        db.session.commit()
        return redirect(url_for("event.events"))

    return render_template("events/edit_event.html", event=event_to_edit, event_date=event_date)


@event.route("/events/<int:event_id>/delete")
def delete_event(event_id):
    event_to_delete = db_find_first(Event, id=event_id)
    db.session.delete(event_to_delete)
    db.session.commit()
    return redirect(url_for("event.events"))


@event.route("/profile/<uuid>")
def profile(uuid):
    user = db_find_first(User, uuid=uuid)

    if uuid == "not_set":
        flash("You must be logged in to view this page.")
        return redirect(url_for("auth.login"))

    if not user:
        abort(404)

    if user.uuid != session.get("user_uuid"):
        flash("You do not have permission to view this profile.")
        abort(403)
        return redirect("error/403.html")

    user_profile = Profile.query.filter_by(user_uuid=user.uuid).first()

    events_created = Event.query.filter_by(creator_id=user.uuid) \
        .order_by(Event.date)

    events_attending = Event.query.join(Attendance) \
        .filter_by(user_id=user.id) \
        .order_by(Event.date)

    return render_template("profile.html", user=user, profile=user_profile,
                           created_events=events_created, attending_events=events_attending)
