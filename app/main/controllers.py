from flask import Blueprint, render_template, url_for
from app.logic import project_logic
from app.util.string_literals import route_string_to_display_string

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/index')
@main.route('/')
def index():
    # TODO fix all the links in footer_items to actually point to a page
    return render_template("index.htm")


@main.route('/projects')
def projects():
    veep_projects = project_logic.get_veep_projects()
    veepx_projects = project_logic.get_veepx_projects()
    return render_template("projects.htm",
                           veep_projects=veep_projects,
                           veepx_projects=veepx_projects)

@main.route('/contact_us')
def contact_us():
    return render_template("contact_us.htm")

@main.route('/events')
def events():
    return render_template("events.htm")

@main.route('/apply')
@main.route('/apply/<position>')
def apply(position):
    if position:
        # TODO do something w/ the application
        position_string = route_string_to_display_string(position)
        return render_template("apply.htm", position=position_string)
    else:
        return render_template("apply.htm")