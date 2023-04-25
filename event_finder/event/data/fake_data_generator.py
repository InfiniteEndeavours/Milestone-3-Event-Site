from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash
from faker import Faker
from event_finder import db
from event_finder.event.models import User, Profile, Event, Attendance
from uuid import uuid4

# Create a Faker instance
fake = Faker()


def create_users(num_users):
    """
    Create a number of fake users
    :param num_users:
    :return:
        Doesn't return anything but will add Users and their profile
        to the database
    """
    for i in range(num_users):
        # Create a new profile for the user
        profile = Profile(first_name=fake.first_name(),
                          last_name=fake.last_name())
        # Create a new user with the profile
        user = User(username=fake.user_name(),
                    password=generate_password_hash(fake.password()),
                    uuid=str(uuid4()))  # type: ignore
        # Set the user attribute on the profile
        profile.user = user
        db.session.add(profile)
        db.session.commit()


def create_events(num_events):
    """
    Create a number of fake events
    :param num_events:
    :return:
        Doesn't return anything but will add Events to the database
    """
    for i in range(num_events):
        title = fake.sentence()
        description = fake.text()
        # Create a date between today and 30 days from now
        date = fake.date_between(start_date='today', end_date='+30d')
        # Create a start time in correct format
        start_time = datetime.strptime(fake.time(
            pattern='%H:%M:%S'), '%H:%M:%S').time()
        # Create an end time 2 hours after the start time
        end_time = (datetime.combine(date, start_time)
                    + timedelta(hours=2)).time()
        location = fake.address()
        creator = User.query.order_by(db.func.random()).first()
        # Create the event
        event = Event(title=title, description=description,
                      date=date, start_time=start_time, end_time=end_time,
                      location=location, creator_id=creator.uuid)
        db.session.add(event)
        db.session.commit()


def create_attendances(num_attendances):
    """
    Create a number of fake attendances
    :param num_attendances:
    :return:
        Doesn't return anything but will add Attendances to the database
    """
    for i in range(num_attendances):
        user = User.query.order_by(db.func.random()).first()
        event = Event.query.order_by(db.func.random()).first()
        attendance = Attendance(user_id=user.id, event_id=event.id)
        db.session.add(attendance)
        db.session.commit()
