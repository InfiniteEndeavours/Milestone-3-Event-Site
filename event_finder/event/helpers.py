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
