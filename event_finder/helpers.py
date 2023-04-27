from event_finder import db

def db_find_first(model, **kwargs):
    """
    Queries a database model and returns the first result found.

    :param:
    model: SQLAlchemy model Object representing a database table.
    **kwargs: One or more keyword arguments representing the filter criteria.
    The keywords should match the column name and
     the value should be the desired value.
     example: db_find_first(User, username='admin')

    :return
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