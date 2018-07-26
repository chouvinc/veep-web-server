from app.util.models import Project
from sqlalchemy.exc import OperationalError

def get_veep_projects():
    try:
        return Project.query.filter_by(is_veep_x=False).all()
    except OperationalError:
        return []



def get_veepx_projects():
    try:
        return Project.query.filter_by(is_veep_x=True).all()
    except OperationalError:
        return []