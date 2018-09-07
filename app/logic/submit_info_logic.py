from app.util.models import Project, Member, Event
from app import db, app
from app.util.form import ProjectForm, TeamMemberForm, ExecMemberForm, EventForm
from flask import flash, request
from random import randint


def form_handler(form):
    return {
        'project': handle_project,
        'team_member': handle_team_member,
        'executive': handle_executive,
        'event': handle_event
    }[form.id](form)


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
    photo_url = get_random_corgi_url()

    member = Member(
        name=form.team_member_name.data,
        team=form.team_name.data,
        email=form.team_member_email.data,
        role=form.role.data,
        photo_url=photo_url
    )

    db.session.add(member)
    db.session.commit()
    flash('Submitted Team Member!')


def handle_executive(form):
    photo_url = get_random_corgi_url()

    executive = Member(
        name=form.exec_member_name.data,
        team=form.exec_team.data,
        email=form.exec_member_email.data,
        role=form.role.data,
        is_executive=True,
        photo_url=photo_url
    )

    db.session.add(executive)
    db.session.commit()
    flash('Submitted Executive!')


def handle_event(form):
    date = ' '.join([form.event_year.data, form.event_month.data, form.event_day.data])

    event = Event(
        title=form.event_title.data,
        date=date,
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


def get_random_corgi_url():
    integer = randint(1, 5)
    filename = ''.join([app.config['S3_ENDPOINT'], 'static/images/corgi', str(integer), '.jpg'])
    return filename
