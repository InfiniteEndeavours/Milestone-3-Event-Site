from datetime import datetime, time
from event_finder import db
from uuid import uuid4
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Generate a unique id for each user
    uuid = db.Column(db.String(36), unique=True, nullable=False, default=str(uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255))
    admin = db.Column(db.Boolean, default=False)
    profile = db.relationship('Profile', backref='user', uselist=False)
    events_created = db.relationship('Event', backref='creator', lazy='dynamic')

    def get_events_created(self):
        return self.events_created.all()

    def get_id(self):
        return self.uuid


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    user_uuid = db.Column(db.String(36), db.ForeignKey("user.uuid"), unique=True)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow().date())
    start_time = db.Column(db.Time, nullable=False, default=time(hour=9, minute=0))
    end_time = db.Column(db.Time, nullable=False, default=time(hour=17, minute=0))
    location = db.Column(db.String(255), nullable=False)
    creator_id = db.Column(db.String(36), db.ForeignKey("user.uuid"), nullable=False)


class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)