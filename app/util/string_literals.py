# This class holds string literals and utility functions

def route_string_to_display_string(string):
    split = string.split('_')
    return ' '.join(split).title()