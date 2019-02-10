from app.dao import project_dao, member_dao, event_dao
from app.mappers import viewmodel_mapper


def populate_objects_by_type(type):
    if type == 'veep_project':
        projects = project_dao.get_veep_projects()
        return handle_mappings('project', projects)
    elif type == 'veepx_project':
        projects = project_dao.get_veepx_projects()
        return handle_mappings('project', projects)
    elif type == 'executive':
        members = member_dao.get_all_exec_members()
        return handle_mappings('member', members)
    elif type == 'team_member':
        members = member_dao.get_all_team_members()
        return handle_mappings('member', members)
    elif type == 'event':
        events = event_dao.get_all_events()
        return handle_mappings('event', events)


def handle_mappings(key, objects):
    mapped_objects = []

    for object in objects:
        mapped_object = {
            'project': viewmodel_mapper.project_model_to_projectviewmodel,
            'member': viewmodel_mapper.member_model_to_memberviewmodel,
            'event': viewmodel_mapper.event_model_to_eventviewmodel
        }[key](object)

        mapped_objects.append(mapped_object)
    return mapped_objects
