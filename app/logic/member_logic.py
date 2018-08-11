from app.util.models import Member
from sqlalchemy.exc import OperationalError

def get_all_exec_members():
    try:
        executives = Member.query.filter_by(is_executive=True).all()
        return executives
    except OperationalError:
        return []

def get_all_team_members():
    try:
        team_members = Member.query.filter_by(is_executive=False).all()
    except OperationalError:
        return []

# TODO implement specific filters for these queries