from app.dao import project_dao, event_dao, member_dao


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

