def form_handler(form):
    return {
        'project': handle_project(form),
        'team_member': handle_team_member(form),
        'executive': handle_executive(form),
        'event': handle_event(form)
    }[form.select.data]

def handle_project(form):
    print('You handled a project')

def handle_team_member(form):
    print('You handled a team member')

def handle_executive(form):
    print('You handled an executive')

def handle_event(form):
    print('You handled an event')
