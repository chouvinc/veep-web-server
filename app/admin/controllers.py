from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import current_user, login_user
from app.util.form import LoginForm

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
@admin.route('/')
def index():
    if current_user.is_authenticated:
        return render_template("submit.htm")
    else:
        return redirect(url_for('.login'))

@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect(url_for('.index'))
    return render_template('login.htm', title='Sign-up', form=form)



# TODO, the login template should have a form with the following elements:
# 1) A select box to choose which table to write to (projects, execs, students)
# 2) Load the corresponding form (for projects we'd need title, tags, preview snippet, and full description)
# 3) Miscellaneous notes that might be added alongside a project (if there are special circumstances)
@admin.route('/submit', methods=['POST'])
@admin.route('/submit/<table>')
def submit(table):
    # TODO pass in context object to show success or not.
    return render_template("submit.htm")

