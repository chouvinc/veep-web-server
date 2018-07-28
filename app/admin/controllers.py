from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user
from app.util.form import LoginForm, SubmitInfoForm, RegistrationForm
from app.util.models import User
from app import db
from app.logic import submit_info_logic

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
        return redirect(url_for('.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.get_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('.login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('.index'))
    return render_template('login.htm', title='Sign-up', form=form)

@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.index'))

# TODO, the login template should have a form with the following elements:
# 1) A select box to choose which table to write to (projects, execs, students)
# 2) Load the corresponding form (for projects we'd need title, tags, preview snippet, and full description)
# 3) Miscellaneous notes that might be added alongside a project (if there are special circumstances)
@admin.route('/submit', methods=['GET', 'POST'])
def submit():
    if current_user.is_authenticated:
        form = SubmitInfoForm()
        if form.validate_on_submit():
            flash('Submitted!')
            submit_info_logic.form_handler(form)
            return redirect(url_for('.submit'))
        return render_template('submit.htm', title='Submit Information', form=form)
    else:
        return redirect(url_for('.login'))

# Use this endpoint to add new users to the admin portal
@admin.route('/register', methods=['GET', 'POST'])
def register():
    if not current_user.is_authenticated:
        admin_only_msg = "Sorry, only executives are allowed to register other members for the admin portal."
        flash(admin_only_msg)
        return render_template('register.htm', title='Register', admin_only_msg=admin_only_msg)
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registered!')
        return redirect(url_for('.login'))
    return render_template('register.htm', title='Register', form=form)

# TODO: change register to add username/email only, and then check in login if user has a password.
# TODO: If they don't have a password prompt them to create one (so we can continue w/ the execs add other execs paradigm)