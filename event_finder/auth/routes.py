from flask import Blueprint, render_template

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


@auth.route("/register")
def register():
    return render_template("register.html")
