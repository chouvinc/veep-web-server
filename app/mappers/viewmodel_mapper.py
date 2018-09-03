def member_model_to_memberviewmodel(member):
    mapped = get_default_map(member.id,
                             member.name,
                             'Current VEEP Executives' if member.is_executive else 'Current VEEP Members'
                             )

    other_properties = get_unmapped_properties(member, mapped)

    mapped['body'] = ' '.join(other_properties)

    return mapped

def project_model_to_projectviewmodel(project):
    mapped = get_default_map(project.id,
                           project.title,
                           'Current VEEP-X Projects' if project.is_veep_x else 'Current VEEP Projects'
                           )

    other_properties = get_unmapped_properties(project, mapped)

    mapped['body'] = ' '.join(other_properties)

    return mapped

def event_model_to_eventviewmodel(event):
    mapped = get_default_map(event.id,
                             event.title,
                             'Current VEEP Events'
                             )

    other_properties = get_unmapped_properties(event, mapped)

    mapped['body'] = ' '.join(other_properties)

    return mapped

def get_unmapped_properties(obj, map):
    other_properties = []

    # TODO implement this somehow -- for some reason sqlalchemy objects are hard to implement
    # as dictionaries. The idea behind other properties is so that users of the admin portal
    # can know specifically what they're deleting without having to go back to the
    # front pages to verify the content of each object

    return other_properties

def get_default_map(id, title, header_text):
    return {
        'id': id,
        'title': ' '.join(['title:', title]),
        'header_text': ' '.join(['header_text:', header_text])
    }