from flask import Blueprint, render_template, url_for


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/index')
@main.route('/')
def index():
    # TODO fix all the links in footer_items to actually point to a page
    return render_template("index.htm")


@main.route('/projects')
def projects():


	return "Derp"
