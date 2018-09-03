from app.util.models import Event
from sqlalchemy.exc import OperationalError
from flask import flash
from app import db

def get_all_events():
    try:
        return Event.query.all()
    except OperationalError:
        return []

# get results by UTC date range
def get_events_by_date_range(startDate, endDate):
    try:
        return Event.query.filter(Event.date >= startDate and Event.date <= endDate)
    except OperationalError:
        return []

def delete_event_by_id(id):
    try:
        delete_events_by_ids([id])
    except OperationalError:
        flash('Delete failed!')
        return

def delete_events_by_ids(ids):
    try:
        for id in ids:
            project = Event.query.get(id)
            db.session.delete(project)
            db.session.commit()

            flash('Event deleted!')
    except OperationalError:
        flash('Delete failed!')
        return
