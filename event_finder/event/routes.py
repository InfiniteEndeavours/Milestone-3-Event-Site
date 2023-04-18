from flask import Blueprint, render_template, request, redirect, session, flash, url_for
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
    return render_template("events.html", events=event_list)
