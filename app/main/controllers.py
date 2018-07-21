from flask import Blueprint, render_template, url_for


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/index')
@main.route('/')
def index():

    links = [
        {"title": "VEEP", "url": url_for('.index')},
        {"title": "Projects", "url": url_for('.projects')}
        # {"title": "Contact Us", "url": url_for('.contact_us')}
    ]

    return render_template("index.htm", links=links)


@main.route('/projects')
def projects():


	return "Derp"