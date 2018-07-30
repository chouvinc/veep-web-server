from app.util.models import Event
from sqlalchemy.exc import OperationalError
from datetime import datetime

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
