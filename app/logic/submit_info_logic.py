from flask import flash, request
from app.util.models import Project
from app import db
from app.util.form import ProjectForm, TeamMemberForm, ExecMemberForm, EventForm

def form_handler(form):
    return {
        'project': handle_project(form),
        'team_member': handle_team_member(form),
        'executive': handle_executive(form),
        'event': handle_event(form)
    }[form.id]

def handle_project(form):
    # TODO make form for isVeepX
    project = Project(title=form.project_title.data,
                      tags=form.project_tags.data,
                      description=form.project_text.data,
                      is_veep_x=form.project_veepx == 'yes')

    db.session.add(project)
    db.session.commit()
    flash('Submitted Project!')

def handle_team_member(form):
    flash('You handled a team member')

def handle_executive(form):
    flash('You handled an executive')

def handle_event(form):
    flash('You handled an event')

def get_fields_for(formtype):
    return {
        'project': ProjectForm(request.form),
        'team_member': TeamMemberForm(request.form),
        'executive': ExecMemberForm(request.form),
        'event': EventForm(request.form)
    }[formtype]