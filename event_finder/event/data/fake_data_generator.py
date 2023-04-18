from datetime import datetime, time, timedelta
from faker import Faker
from event_finder import db
from event_finder.event.models import User, Profile, Event, Attendance
from uuid import uuid4

fake = Faker()


def create_users(num_users):
    for i in range(num_users):
        # Create a new profile for the user
        profile = Profile(first_name=fake.first_name(), last_name=fake.last_name())
        # Create a new user with the profile
        user = User(username=fake.user_name(), password=fake.password(), uuid=str(uuid4()))  # type: ignore
        # Set the user attribute on the profile
        profile.user = user
        db.session.add(profile)
        db.session.commit()


def create_events(num_events):
    for i in range(num_events):
        title = fake.sentence()
        description = fake.text()
        date = fake.date_between(start_date='today', end_date='+30d')
        start_time = datetime.strptime(fake.time(pattern='%H:%M:%S'), '%H:%M:%S').time()
        end_time = (datetime.combine(date, start_time) + timedelta(hours=2)).time()
        location = fake.address()
        creator = User.query.order_by(db.func.random()).first()
        event = Event(title=title, description=description, date=date, start_time=start_time, end_time=end_time,
                      location=location, creator_id=creator.uuid)
        db.session.add(event)
        db.session.commit()


def create_attendances(num_attendances):
    for i in range(num_attendances):
        user = User.query.order_by(db.func.random()).first()
        event = Event.query.order_by(db.func.random()).first()
        attendance = Attendance(user_id=user.id, event_id=event.id)
        db.session.add(attendance)
        db.session.commit()
