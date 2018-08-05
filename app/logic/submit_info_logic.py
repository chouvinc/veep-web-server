from flask import flash, request
from app.util.models import Project, Member, Event
from app import db
from app.util.form import ProjectForm, TeamMemberForm, ExecMemberForm, EventForm
from app.logic import email_logic
from config import Config

def form_handler(form):
    return {
        'project': handle_project(form),
        'team_member': handle_team_member(form),
        'executive': handle_executive(form),
        'event': handle_event(form)
    }[form.id]

def handle_project(form):
    project = Project(
        title=form.project_title.data,
        tags=form.project_tags.data,
        description=form.project_text.data,
        is_veep_x=form.project_veepx.data == 'yes'
    )

    db.session.add(project)
    db.session.commit()
    flash('Submitted Project!')

def handle_team_member(form):
    member = Member(
        name=form.team_member_name.data,
        team=form.team_name.data,
        email=form.team_member_email.data,
        role=form.role.data
    )

    db.session.add(member)
    db.session.commit()
    flash('Submitted Team Member!')

def handle_executive(form):
    executive = Member(
        name=form.exec_member_name.data,
        team=form.exec_team.data,
        email=form.exec_member_email.data,
        role=form.role.data,
        is_executive=True,
        username=form.exec_username.data
    )

    # TODO set it so that adding an exec generates a temporary URL that'll let them set their password
    #user = User(username=form.exec_username.data, email=form.exec_member_email.data)
    #user.set_password(Config.TEMP_PASSWORD)

    #email_logic.send_set_password_email(user.email)

    db.session.add(executive)
    db.session.commit()
    flash('Submitted Executive!')

def handle_event(form):
    event = Event(
        title=form.event_title.data,
        date=form.event_date.data,
        location=form.event_location.data,
        desc=form.event_desc.data
    )

    db.session.add(event)
    db.session.commit()
    flash('Submitted Event!')

def get_fields_for(formtype):
    return {
        'project': ProjectForm(request.form),
        'team_member': TeamMemberForm(request.form),
        'executive': ExecMemberForm(request.form),
        'event': EventForm(request.form)
    }[formtype]