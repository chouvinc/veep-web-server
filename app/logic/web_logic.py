from app.dao import project_dao, member_dao


def get_all_projects():
    return project_dao.get_veep_projects(), project_dao.get_veepx_projects()


def get_all_members():
    project_title_list = get_project_names_from_projects()
    team_list = []
    executives = member_dao.get_all_exec_members()

    for title in project_title_list:
        members = member_dao.get_members_by_project(title)

        for member in members:
            # need to be careful here, if we commit the member now it could overwrite the old data
            member.role = snake_case_to_title(member.role)

        team_list.append({"name": title, "members": members})

    return executives, team_list


def get_project_names_from_projects():
    # TODO: did this in a rush so we're getting all projects first, then getting the filtered results from the DAO.
    # TODO: replace this w/ a foreign key constraint instead + relationship so we can get both objects in 1 query
    veep, veepx = get_all_projects()
    all_projects = veep + veepx

    if all_projects:
        return list(map(lambda project: project.title, all_projects))
    else:
        return []


def snake_case_to_title(snake_case_string):
    split = snake_case_string.split('_')
    if split:
        return ' '.join(word.title() for word in split)
    else:
        # String is already in proper format
        return snake_case_string