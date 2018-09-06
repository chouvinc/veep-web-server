from flask import Blueprint, render_template, flash, request, url_for, redirect
from app.logic import email_logic, web_logic
from app.util.string_literals import route_string_to_display_string
from app.util.form import ContactUsForm

main = Blueprint('main', __name__, template_folder='templates')


@main.route('/index')
@main.route('/')
def index():
    # TODO fix all the links in footer_items to actually point to a page
    return render_template("index.htm")


@main.route('/projects')
def projects():
    veep_projects, veepx_projects = web_logic.get_all_projects()
    return render_template("projects.htm",
                           veep_projects=veep_projects,
                           veepx_projects=veepx_projects)


@main.route('/contact_us', methods=['GET', 'POST'])
def contact_us():
    form = ContactUsForm()

    if request.method == 'GET':
        return render_template("contact_us.htm", form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            flash('Emailed!')
            email_logic.form_handler(form)
            return redirect(url_for('.contact_us'))
        else:
            flash('Email failed...')
            return render_template("contact_us.htm", form=form)


@main.route('/events')
def events():
    events = web_logic.get_all_events()
    return render_template("events.htm", events=events)


@main.route('/apply/<position>')
def apply_position(position):
    # TODO link to google forms instead of rendering template
    position_string = route_string_to_display_string(position)
    return render_template("apply.htm", position=position_string)


@main.route('/our_team')
def our_team():
    executives, teams = web_logic.get_all_members()
    return render_template("our_team.htm", executives=executives, teams=teams)
