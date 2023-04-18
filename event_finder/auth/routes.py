from flask import Blueprint, render_template, request, redirect, session, flash, url_for
from event_finder import db
from event_finder.event.models import User, Profile
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint("auth", __name__, template_folder="../event_finder/templates")


# Helper Functions

def validate_password(password, password_confirm):
    """
    Validates a user's password and password confirmation.

    Args:
        password: String representing the user's password.
        password_confirm: String representing the user's password confirmation.

    Returns:
        A string indicating the result of the validation. If the passwords match and meet
        the required criteria, the function returns "valid". If the passwords do not match,
        the function returns "no_match". If the password does not meet the
        required criteria, the function returns "not_complex_enough".
    """
    # Check if passwords match and are valid
    if password != password_confirm:
        return "no_match"
    if not (any(x.isupper() for x in password) and
            any(x.islower() for x in password) and
            any(x.isdigit() for x in password) and
            any(x in list("!@#$%^&*()_+{}|:'<>?-=[]\\;,./`~]*") for x in password)):
        return "not_complex_enough"
    return "valid"


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Store user input as variables
        username: str = request.form.get('username').lower()
        first_name: str = request.form.get('fname')
        last_name: str = request.form.get('lname')
        form_password: str = request.form.get('password')
        form_password_confirm: str = request.form.get('confirm-password')

        # Check if username is already registered
        existing_user_check = User.query.filter_by(username=username).first()
        if existing_user_check:
            flash("Username already exists. Please try again.")
            return redirect(url_for("auth.register"))

        # Check if passwords match and are valid
        valid_password = validate_password(form_password, form_password_confirm)

        # Declare a variable to store the password hash
        password_hash = ""

        # If the password is not valid, flash an error message
        if valid_password == "no_match":
            flash("The passwords you entered do not match.")
            return redirect(url_for('auth.register'))
        elif valid_password == "not_complex_enough":
            flash("The password you have entered is not complex enough."
                  "It requires at least one uppercase, one lowercase, one digit and a special character.")
            return redirect(url_for('auth.register'))
        elif valid_password == "valid":
            # Generates a password hash using pbkdf2:sha256 algorithm, iterates 150000 times, salts with a length of 20
            password_hash = generate_password_hash(form_password, method='pbkdf2:sha256:150000', salt_length=20)

        # Create a new user
        new_user = User(username=username, password=password_hash)
        db.session.add(new_user)
        db.session.commit()

        # Create a new profile
        new_profile = Profile(first_name=first_name, last_name=last_name, user_uuid=new_user.uuid)
        db.session.add(new_profile)
        db.session.commit()

        # Add a "user" session cookie
        registered_user = User.query.filter_by(username=username).first()
        session["user_uuid"] = registered_user.uuid

        # Redirect to the user's profile page
        return redirect(url_for('event.index'))

    return render_template("register.html")
