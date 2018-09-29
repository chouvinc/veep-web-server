from app.mappers import viewmodel_mapper
from app.dao import project_dao, event_dao, member_dao


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

def get_delete_logic(key):
    # return the function reference depending on what type we get
    return {
        'veep_project': project_dao.delete_projects_by_ids,
        'veepx_project': project_dao.delete_projects_by_ids,
        'executive': member_dao.delete_members_by_ids,
        'team_member': member_dao.delete_members_by_ids,
        'event': event_dao.delete_events_by_ids
    }[key]

def delete_selected_objects(type, ids):
    # primary keys have to be integers
    # TODO handle what happens on delete failure
    ids = list(map(str, ids))

    del_function = get_delete_logic(type)
    del_function(ids)

