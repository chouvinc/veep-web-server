from app.util.models import Member
from sqlalchemy.exc import OperationalError
from flask import flash
from app import db


#TODO consider using a class that extends common functionality
def get_all_exec_members():
    try:
        executives = Member.query.filter_by(is_executive=True).all()
        return executives
    except OperationalError:
        return []


def get_all_team_members():
    try:
        team_members = Member.query.filter_by(is_executive=False).all()
        return team_members
    except OperationalError:
        return []


def get_members_by_project(filter):
    try:
        team_members = Member.query.filter_by(team=filter).all()
        return team_members
    except OperationalError:
        return []


def delete_member_by_id(id):
    try:
        delete_members_by_ids([id])
    except OperationalError:
        flash('Delete failed!')
        return


def delete_members_by_ids(ids):
    try:
        for id in ids:
            project = Member.query.get(id)
            db.session.delete(project)
            db.session.commit()

            flash('Member deleted!')
    except OperationalError:
        flash('Delete failed!')
        return

