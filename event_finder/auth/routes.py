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
    """
    Flask view function that handles requests to register a new user. It accepts both GET and POST requests to the
    /register route.

    When a POST request is received, it processes the user input from the registration form, validates the input,
     creates a new user, and adds the user to the database.
     It also creates a new profile for the user and sets a session cookie to log the user in.
    If the request is a GET request, it simply renders the registration page.

    Returns:
        If the request is a GET request, returns the rendered "register.html" template.
        If the request is a POST request and user input is valid, redirects to the index page.
        If the request is a POST request and user input is invalid, redirects back to the registration
         page and displays an error message.
    """
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


@auth.route("/login", methods=["GET", "POST"])
def login():
    """
        Logs in a user.

        If a GET request is received, render the login form. If a POST request is received, validate user credentials
        and log in the user if they are valid.

        Returns:
            A rendered HTML template if a GET request is received, or a direct response if a POST request is received.
    """
    if request.method == "POST":
        username: str = request.form.get('username').lower()
        password: str = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user:
            # Check if user inputted password matches hashed password in DB
            if check_password_hash(user.password, password):
                # Add uuid as a session cookie
                session["user_uuid"] = user.uuid
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
            flash("Incorrect Username/Password."
                  "If you have forgotten your details, please register a new account.")
            return render_template("login.html")

    return render_template("login.html")


@auth.route("/logout")
def logout():
    """
        Logs out a user.

        Removes the session cookies and redirects to the login page.
    """
    session.pop("user_uuid", None)

    if "admin" in session:
        session.pop("admin", None)

    flash("You have been logged out.")
    return redirect(url_for("auth.login"))
