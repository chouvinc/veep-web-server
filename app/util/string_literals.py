# This class holds string literals and utility functions
set_password_email_string = """"Welcome aboard the exec team! 
Please follow this link to set a new password: %s ."""


def route_string_to_display_string(string):
    split = string.split('_')
    return ' '.join(split).title()

def get_set_password_link(user, hash):
    return "Not implemented yet."