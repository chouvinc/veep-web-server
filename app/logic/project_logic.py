from app.util.models import Project
from sqlalchemy.exc import OperationalError
from flask import flash
from app import db

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

def delete_project_by_id(id):
    try:
        delete_projects_by_ids([id])
    except OperationalError:
        flash('Delete failed!')
        return

def delete_projects_by_ids(ids):
    try:
        for id in ids:
            project = Project.query.get(id)
            db.session.delete(project)
            db.session.commit()

            flash('Project deleted!')
    except OperationalError:
        flash('Delete failed!')
        return
