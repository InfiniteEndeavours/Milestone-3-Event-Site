from flask import (Blueprint, render_template,
                   request, redirect, session, flash, url_for)
from event_finder import db
from event_finder.event.models import User, Profile
from event_finder.helpers import validate_password, validate_form_data
from werkzeug.security import generate_password_hash, check_password_hash
from uuid import uuid4

auth = Blueprint("auth", __name__,
                 template_folder="../event_finder/templates")


@auth.route("/register", methods=["GET", "POST"])
def register():
    """
    Route to handle requests to register a new user.

     Accepts both GET and POST requests.

    When POST request is recieved, it will process user input
     from the form and then validate the input.
    When the input is determined to be valid, the user is
     created, assigned a session
     cookie and returned to the profile page.
     If the request is a GET request (page load),
      it will render the registration page.

     Returns:
        If the request is a GET request, returns the rendered
         version of "register.html" template.
        If the request is a POST request and the user input
         is valid, then login,
         assign session cookie and redirect to profile page.
        If the request is a POST request and the user input
         is invalid, then redirect the user
        to registration page and flash an error
    """
    if request.method == "POST":
        # Store user input as variables
        username: str = request.form.get('username').lower()
        first_name: str = request.form.get('fname')
        last_name: str = request.form.get('lname')
        form_password: str = request.form.get('password')
        form_password_confirm: str = request.form.get('confirm-password')

        form_data = request.form
        is_valid, message = validate_form_data(form_data, "registration")
        if not is_valid:
            flash(message)
            return redirect(url_for("auth.register", username=username,
                                    first_name=first_name,
                                    last_name=last_name))

        # Check if username is already registered
        existing_user_check = User.query.filter_by(username=username).first()
        if existing_user_check:
            flash("Username already exists. Please try again.")
            return redirect(url_for("auth.register", first_name=first_name,
                                    last_name=last_name))

        # Check if passwords match and are valid
        valid_password = validate_password(
            form_password, form_password_confirm)
        # Declare a variable to store the password hash
        password_hash = ""

        # If the password is not valid, flash an error message
        if valid_password == "no_match":
            flash("The passwords you entered do not match.")
            return redirect(url_for('auth.register', username=username,
                                    first_name=first_name,
                                    last_name=last_name))
        elif valid_password == "not_complex_enough":
            flash(
                "The password you have entered is not complex enough."
                "It requires at least one uppercase, one lowercase,"
                " one digit and a special character.")
            return redirect(url_for('auth.register', username=username,
                                    first_name=first_name,
                                    last_name=last_name))
        elif valid_password == "valid":
            # Generates a password hash using pbkdf2:sha256 algorithm, iterates
            # 150000 times, salts with a length of 20
            password_hash = generate_password_hash(
                form_password, method='pbkdf2:sha256:150000', salt_length=20)

        # Create a new user
        new_user = User(username=username, password=password_hash,
                        uuid=str(uuid4()))
        db.session.add(new_user)
        # Create a new profile
        new_profile = Profile(
            first_name=first_name,
            last_name=last_name,
            user_uuid=new_user.uuid)
        db.session.add(new_profile)
        db.session.commit()

        # Add a "user" session cookie
        registered_user = User.query.filter_by(username=username).first()
        session["user_uuid"] = registered_user.uuid

        # Redirect to the user's profile page
        return redirect(url_for('event.index'))

    return render_template("auth/register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    Log in a user.

        If a GET request is received, render the login form.
         If a POST request is received, validate user credentials
        and log in the user if they are valid.

        Returns:
            A rendered HTML template if a GET request is received,
             or a direct response if a POST request is received.
    """
    if request.method == "POST":
        username: str = request.form.get('username').lower()
        password: str = request.form.get('password')

        form_data = request.form
        is_valid, message = validate_form_data(form_data, "login")
        if not is_valid:
            flash(message)
            return redirect(url_for("auth.login"))

        user = User.query.filter_by(username=username).first()

        if user:
            # Check if user inputted password matches hashed password in DB
            if check_password_hash(user.password, password):
                # Add uuid as a session cookie
                session["user_uuid"] = user.uuid
                # If a user is an admin, add admin session cookie
                if user.admin:
                    session["admin"] = True

                flash("You are now logged in.")
                return redirect(url_for("event.index"))
            else:
                # If password doesn't match the password hash then redirect
                flash("Incorrect Username/Password.")
                return redirect(url_for("auth.login"))
        else:
            # If username doesn't exist return to login page
            flash(
                "Incorrect Username/Password."
                "If you have forgotten your details,"
                " please register a new account.")
            return render_template("auth/login.html")

    return render_template("auth/login.html")


@auth.route("/logout")
def logout():
    """
    Log out a user.

    Removes the session cookies and redirects to the login page.

    :returns:
        Login.html
    """
    if session.keys:
        for key in list(session.keys()):
            session.pop(key)
        flash("You have been logged out.")

    return redirect(url_for("auth.login"))
