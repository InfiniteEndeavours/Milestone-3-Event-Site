from event_finder import db
from datetime import datetime

event_form_types = {
    "title": (str, None),
    "description": (str, None),
    "location": (str, None),
    "date": (datetime, "%Y-%m-%d"),
    "start_time": (datetime, "%H:%M"),
    "end_time": (datetime, "%H:%M")
}

registration_form_types = {
    "username": (str, None),
    "fname": (str, None),
    "lname": (str, None),
    "password": (str, None),
    "confirm-password": (str, None),
}

login_form_types = {
    "username": (str, None),
    "password": (str, None)
}


def db_find_first(model, **kwargs):
    """
    Queries a database model and returns the first result found.

    :param:
    model: SQLAlchemy model Object representing a database table.
    **kwargs: One or more keyword arguments representing the filter criteria.
    The keywords should match the column name and
     the value should be the desired value.
     example: db_find_first(User, username='admin')

    :return:
    The first row from the query that matches the filter criteria,
     or None if no matching row is found.
    """
    return model.query.filter_by(**kwargs).first()


def validate_password(password, password_confirm):
    """
    Validate a user's password and password confirmation.

    Args:
        password: String representing the user's password.
        password_confirm: String representing the user's password confirmation.

    Returns:
        - "valid" if the passwords match and also meet the criteria.
        - "no_match" if the passwords do not match.
        - "not_complex_enough" if the password does not
         feature special characters.
    """
    # Check if passwords match and are valid
    if password != password_confirm:
        return "no_match"
    if not (any(x.isupper() for x in password) and
            any(x.islower() for x in password) and
            any(x.isdigit() for x in password) and
            any(x in list("!@#$%^&*()_+{}|:'<>?-=[]\\;,./`~]*")
                for x in password)):
        return "not_complex_enough"
    return "valid"


def validate_form_data(form_data, form_type):
    """
    Validate the form data according to specified form type.

    :param:
        form_data: Dictionary containing data from form.
        form_type: String to represent a form type. "event",
         "registration" and "login" are all valid
          options for form_type.

    :returns:
        Tuple with two elements; The first is a boolean to
         indicate if validation was successful or not.
          The second is a message to show the result
           of the validation.

    """
    if form_type == "event":
        required_fields = event_form_types
    elif form_type == "registration":
        required_fields = registration_form_types
    elif form_type == "login":
        required_fields = login_form_types
    else:
        return False, "Unknown Form"

    # Iterate over each field in required_fields dictionary
    for field_name, (field_type, field_format) in required_fields.items():
        # Obtain value from form_data dictionary
        value = form_data.get(field_name)

        if field_type == datetime:
            try:
                datetime.strptime(value, field_format)
            except ValueError:
                return False, f"Invalid format for" \
                              f" {field_name}, got {value}," \
                              f" expected {field_format}"
        # Check that value has correct data type
        elif not isinstance(value, field_type):
            # Return false and an error message if data type is incorrect
            return False, f"Invalid type on" \
                          f" {field_name}. Expected {field_type}," \
                          f" got {type(value)}"
    return True, "All fields are valid"
