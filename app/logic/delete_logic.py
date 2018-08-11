from app.mappers import viewmodel_mapper
from app.logic import event_logic, project_logic, member_logic

def populate_objects_by_type(type):
    if type == 'veep_project':
        projects = project_logic.get_veep_projects()
        return handle_mappings('project', projects)
    elif type == 'veepx_project':
        projects = project_logic.get_veepx_projects()
        return handle_mappings('project', projects)
    elif type == 'executives':
        members = member_logic.get_all_exec_members()
        return handle_mappings('member', members)
    elif type == 'team_member':
        members = member_logic.get_all_team_members()
        return handle_mappings('member', members)
    elif type == 'event':
        events = event_logic.get_all_events()
        return handle_mappings('event', events)

def handle_mappings(key, objects):
    mapped_objects = []

    for object in objects:
        mapped_object = {
            'project': viewmodel_mapper.project_model_to_projectviewmodel(object),
            'member': viewmodel_mapper.member_model_to_memberviewmodel(object),
            'event': viewmodel_mapper.event_model_to_eventviewmodel(object)
        }[key]

        mapped_objects.append(mapped_object)
    return mapped_objects
