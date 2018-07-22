from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.util.form import LoginForm
from app.util.models import User

admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
@admin.route('/')
def index():
    if current_user.is_authenticated:
        return render_template("admin.htm")
    else:
        return redirect(url_for('.login'))

@admin.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('.admin'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('.login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('.admin'))
    return render_template('login.htm', title='Sign-up', form=form)

@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('/'))

# TODO, the login template should have a form with the following elements:
# 1) A select box to choose which table to write to (projects, execs, students)
# 2) Load the corresponding form (for projects we'd need title, tags, preview snippet, and full description)
# 3) Miscellaneous notes that might be added alongside a project (if there are special circumstances)
@admin.route('/submit', methods=['POST'])
@admin.route('/submit/<table>')
def submit(table):
    # TODO pass in context object to show success or not.
    return render_template("admin.htm")

