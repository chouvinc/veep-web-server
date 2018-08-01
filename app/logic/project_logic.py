from app.util.models import Project
from sqlalchemy.exc import OperationalError

def get_veep_projects():
    try:
        projects = Project.query.filter_by(is_veep_x=False).all()
        return projects
    except OperationalError:
        return []



def get_veepx_projects():
    try:
        projects = Project.query.filter_by(is_veep_x=True).all()
        return projects
    except OperationalError:
        return []