from flask import (Blueprint, render_template, redirect,
                   session, flash, url_for, abort)
from event_finder import db
from event_finder.event.models import Event, User, Attendance
from event_finder.helpers import db_find_first

admin = Blueprint("admin", __name__,
                  template_folder="../event_finder/templates")


@admin.route('/admin')
def admin_page():
    """
    admin_page function.

    If the user who loads the page is an admin, they are shown the admin page,
    else they are diverted to a 403 and told they are not authorised.

    :return:
        admin.html if authorised
        403.html if unauthorised
    """
    uuid = session.get("user_uuid")
    user = db_find_first(User, uuid=uuid)
    if user.admin:
        event_list = Event.query.all()
        return render_template("admin/admin.html", events=event_list)
    else:
        abort(403)
        flash("You are not authorized to view this page.")
        return redirect("error/403.html")


@admin.route('/admin/delete-event/<int:event_id>', methods=["POST"])
def delete_event(event_id):
    """
    Admin delete event.

    If the admin chooses to delete an event, the event ID is passed in
    to the db_find_first helper function. This queries the
    event table to find the matching event. Then all
    entries relating to the event in the attendance table are deleted.
    This is a prerequisite to deleting the event from the Event table.
    :return:
        admin.html with a flash confirming deletion
    """
    event = db_find_first(Event, id=event_id)
    Attendance.query.filter_by(event_id=event.id).delete()
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted.")
    return redirect(url_for("admin.admin_page"))
