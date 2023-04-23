from flask import Blueprint, render_template, redirect, session, flash, url_for, abort
from event_finder import db
from event_finder.event.models import Event, User, Attendance
from event_finder.event.helpers import db_find_first

admin = Blueprint("admin", __name__, template_folder="../event_finder/templates")


@admin.route('/admin')
def admin_page():
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
    event = db_find_first(Event, id=event_id)
    Attendance.query.filter_by(event_id=event.id).delete()
    db.session.delete(event)
    db.session.commit()
    flash("Event deleted.")
    return redirect(url_for("admin.admin_page"))
