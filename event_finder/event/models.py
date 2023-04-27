from datetime import datetime, time
from event_finder import db
from uuid import uuid4


# User Model
class User(db.Model):
    """User model for storing user related details."""

    id = db.Column(db.Integer, primary_key=True)
    # Generate a unique id for each user using uuid4 template
    uuid = db.Column(db.String(36), unique=True,
                     nullable=False, default=str(uuid4()))
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255))
    admin = db.Column(db.Boolean, default=False)
    # One-to-One relationship with Profile
    profile = db.relationship('Profile',
                              backref='user', uselist=False)
    # One-to-Many relationship with Event
    events_created = db.relationship('Event',
                                     backref='creator', lazy='dynamic')


# Profile Model
class Profile(db.Model):
    """Profile model for storing user profile related details."""

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # Foreign key to User.uuid
    user_uuid = db.Column(db.String(36),
                          db.ForeignKey("user.uuid"), unique=True)


# Event Model
class Event(db.Model):
    """Event model for storing event related details."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime, nullable=False,
                     default=datetime.utcnow().date())
    start_time = db.Column(db.Time, nullable=False,
                           default=time(hour=9, minute=0))
    end_time = db.Column(db.Time, nullable=False,
                         default=time(hour=17, minute=0))
    location = db.Column(db.String(255), nullable=False)
    # Foreign key to User.uuid
    creator_id = db.Column(db.String(36),
                           db.ForeignKey("user.uuid"), nullable=False)


# Attendance Model
class Attendance(db.Model):
    """Attendance model for storing attendance related details."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
