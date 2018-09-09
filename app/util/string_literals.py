# This class holds string literals and utility functions

# Email strings
SET_PASSWORD_EMAIL_STRING = """Welcome aboard the exec team! 
Please follow this link to login: %s . 
Your username is: %s
Your temporary password is: %s
After signing in please follow this link to change your password: %s
"""
WEBSITE_PREFIX = "[Website]: "
BASEURL = 'https://uoftveep.herokuapp.com/'


def route_string_to_display_string(string):
    split = string.split('_')
    return ' '.join(split).title()

def get_set_password_link(user, hash):
    return "Not implemented yet."
