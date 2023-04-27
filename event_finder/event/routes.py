from flask import (Blueprint, render_template, request,
                   redirect, session, flash, url_for, abort)
from event_finder import db
from datetime import datetime
from event_finder.event.models import Event, User, Profile, Attendance
from event_finder.helpers import db_find_first, validate_form_data
import random

event = Blueprint("event", __name__,
                  template_folder="../event_finder/templates")


@event.route("/")
def index():
    """
    Route returns the index page with two random events.

    :return:
        event_one - The first random event
        event_two - The second random event
        render_template("index.html")
    """
    current_events = list(Event.query.filter(
        Event.date >= datetime.utcnow()).all())
    if current_events:
        # Use random to generate a random number between 0
        # and the length of current_events -1
        event_one = current_events[random.randint(0, len(current_events) - 1)]
        event_two = current_events[random.randint(0, len(current_events) - 1)]
        return render_template("index.html",
                               event_one=event_one, event_two=event_two)
    return render_template("index.html")


@event.route("/events")
def events():
    """
    Route returns the events page with a list of all events.

    :return:
        event_list - A list of all events
        render_template("events/events.html")
    """
    page = request.args.get('page', 1, type=int)
    current_date = datetime.utcnow().date()
    event_list = Event.query.filter(Event.date >= current_date) \
        .order_by(Event.date).paginate(page=page, per_page=10)
    return render_template("events/events.html", events=event_list)


@event.route("/events/<int:event_id>")
def event_info(event_id):
    """
    Route returns the event info page for a specific event.

    :param event_id:
    :return:
        event_data - The event data for the event
        render_template("events/event_info.html")
    """
    event_data = db_find_first(Event, id=event_id)
    # If the event doesn't exist, return a 404 error
    if not event_data:
        abort(404)

    user = db_find_first(User, uuid=session.get("user_uuid"))
    # If the user is logged in, check if they are registered for the event
    if user:
        existing_registration = Attendance.query \
            .filter_by(user_id=user.id, event_id=event_id).first()
        return render_template("events/event_info.html",
                               event=event_data,
                               existing_registration=existing_registration)

    return render_template("events/event_info.html", event=event_data)


@event.route("/events/create_event", methods=["GET", "POST"])
def create_event():
    """
     Route returns the create event page.

    :return:
        render_template("events/create_event.html") on GET request
        render_template("events/create_event.html") on failed POST request
        redirect(url_for("event.events")) on POST request
    """
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
        start_time = datetime.strptime(request.form.get("start_time"),
                                       "%H:%M").time()
        end_time = datetime.strptime(request.form.get("end_time"),
                                     "%H:%M").time()

        form_data = request.form
        is_valid, message = validate_form_data(form_data, "event")
        if not is_valid:
            flash(message)
            return redirect(url_for("event.create_event"))

        date = datetime.strptime(date, "%Y-%m-%d").date()

        # Check if the event date is in the past
        if date < datetime.utcnow().date():
            flash("Event date must be in the future.")
            return render_template("events/create_event.html")

        # Check if all fields are filled out
        event_fields = [title, description,
                        location, date, start_time, end_time]
        for field in event_fields:
            if not field:
                flash(f"Please fill out the required fields.")
                return render_template("events/create_event.html")
        new_event = Event(title=title, description=description,
                          location=location, date=date,
                          start_time=start_time, end_time=end_time,
                          creator_id=user.uuid)
        db.session.add(new_event)
        db.session.commit()
        flash("Event created successfully.")
        return redirect(url_for("event.events"))

    return render_template("events/create_event.html")


@event.route("/events/<int:event_id>/edit_event", methods=["GET", "POST"])
def edit_event(event_id):
    """
    Route returns the edit event page.

    Form fields are pre-populated with the event data.
    :param event_id:
    :return:
        event_to_edit - The event data for the event
        event_date - The event date in the format YYYY-MM-DD
        event_start_date - The event start time in the format HH:MM
        event_end_date - The event end time in the format HH:MM
        render_template("events/edit_event.html") on GET request
        redirect(url_for("event.events")) on POST request

    """
    event_to_edit = db_find_first(Event, id=event_id)
    event_date = event_to_edit.date.strftime("%Y-%m-%d")
    event_start_date = event_to_edit.start_time.strftime("%H:%M")
    event_end_date = event_to_edit.end_time.strftime("%H:%M")
    if request.method == "POST":
        event_to_edit.title = request.form.get("title")
        event_to_edit.description = request.form.get("description")
        event_to_edit.location = request.form.get("location")
        event_to_edit.date = request.form.get("date")
        event_to_edit.start_time = request.form.get("start_time")
        event_to_edit.end_time = request.form.get("end_time")

        form_data = request.form
        is_valid, message = validate_form_data(form_data, "event")
        if not is_valid:
            flash(message)
            return redirect(url_for("event.edit_event", event_id=event_id))

        db.session.add(event_to_edit)
        db.session.commit()
        return redirect(url_for("event.events"))

    return render_template("events/edit_event.html",
                           event=event_to_edit, event_date=event_date,
                           event_start_date=event_start_date,
                           event_end_date=event_end_date)


@event.route("/events/<int:event_id>/delete")
def delete_event(event_id):
    """
    Route deletes an event and all associated attendance records.

    :param event_id:
    :return:
        redirect(url_for("event.events"))
    """
    event_to_delete = db_find_first(Event, id=event_id)
    Attendance.query.filter_by(event_id=event_to_delete.id).delete()
    db.session.delete(event_to_delete)
    db.session.commit()
    return redirect(url_for("event.events"))


@event.route("/events/<int:event_id>/register")
def event_registration(event_id):
    """
    Route registers a user for an event.

    Redirects user to the event info page on click.
    :param event_id:
    :return:
        redirect(url_for("event.event_info", event_id=event_id))
    """
    user = db_find_first(User, uuid=session.get("user_uuid"))
    registration = Attendance.__table__.insert() \
        .values(user_id=user.id, event_id=event_id)
    db.session.execute(registration)
    db.session.commit()
    flash("You are now registered for this event.")
    return redirect(url_for("event.event_info", event_id=event_id))


@event.route("/events/<int:event_id>/unregister")
def event_deregister(event_id):
    """
     Route deregisters a user from an event.

    Redirects user to the event info page on click.

    :param event_id:
    :return:
        redirect(url_for("event.event_info", event_id=event_id))
    """
    user = db_find_first(User, uuid=session.get("user_uuid"))
    db.session.execute(Attendance.__table__.delete().filter(
        Attendance.user_id == user.id, Attendance.event_id == event_id))
    db.session.commit()
    flash("You are now unregistered from this event.")
    return redirect(url_for("event.event_info", event_id=event_id))


@event.route("/profile/<uuid>")
def profile(uuid):
    """
    Route returns the profile page.

    :param uuid:
    :return:
        user_profile - The profile data for the user
        events_created - The events created by the user
        events_attending - The events the user is attending
        render_template("profile.html")
    """
    user = db_find_first(User, uuid=uuid)

    if uuid == "not_set":
        flash("You must be logged in to view this page.")
        return redirect(url_for("auth.login"))

    if not user:
        abort(404)
        return redirect(url_for("auth.login"))

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
                           created_events=events_created,
                           attending_events=events_attending)
