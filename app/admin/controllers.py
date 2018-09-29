from flask import Blueprint, request, render_template, redirect, url_for, flash, jsonify
from flask_login import current_user, login_user, logout_user
from app.util.form import LoginForm, RegistrationForm, ChangePasswordForm
from app.util.models import User
from app import db
from app.logic import submit_info_logic, delete_logic, edit_info_logic, email_logic
from app.mappers.display_string_mapper import map

import datetime
import hashlib

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


@admin.route('/submit')
def submit():
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))
    return render_template('submit.htm', title='Submit', init_page=True)


@admin.route('/submit/<type>', methods=['GET', 'POST'])
def submit_type(type):
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))

    form = submit_info_logic.get_fields_for(type)

    if form.validate_on_submit():
        submit_info_logic.form_handler(form)
        return redirect(url_for('.submit'))

    return render_template('submit.htm', title='Submit', form=form, type=type)


@admin.route('/delete')
def delete():
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))

    return render_template('delete.htm',
                           title='Delete',
                           delete_objects=None,
                           init_page=True)


@admin.route('/delete/<type>', methods=['GET', 'POST'])
def delete_type(type):
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))

    if request.method == 'POST':
        # JSON being sent through AJAX.
        json = request.get_json()

        type = json['type']
        ids_to_delete = json['ids']

        delete_logic.delete_selected_objects(type, ids_to_delete)
        # This isn't a request from Flask's request context, will need to manually return
        # a redirect link for AJAX to consume.
        return jsonify({'redirect': url_for('.delete')})
    else:
        delete_objects = delete_logic.populate_objects_by_type(type)

        return render_template('delete.htm',
                               title='Delete',
                               delete_objects=delete_objects,
                               typeString=map[type],
                               type=type)


@admin.route('/edit')
def edit():
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))
    return render_template('edit.htm')


@admin.route('/edit/<type>', methods=['GET', 'POST'])
def edit_type(type):
    # TODO: add generic authentication layer (consider using decorators, I don't know too much about them so will
    # need to research and see what's standard practice). ~Vincent
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))

    form = edit_info_logic.get_fields_for(type)

    if form.validate_on_submit:
        edit_info_logic.form_handler(form)
        flash('Edited!')
        return redirect(url_for('.edit'))

    return render_template('edit.htm', title='Edit', form=form)


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

        # Create a password based on current time
        hash_obj = hashlib.sha1(str(datetime.datetime.now()).encode())
        generated_password = hash_obj.hexdigest()[0:8]
        user.set_password(generated_password)
        db.session.add(user)
        db.session.commit()
        flash('Registered!')

        # Send an email to the user to change their password
        email_logic.send_set_password_email(form.email.data, form.username.data, generated_password)
        return redirect(url_for('.login'))
    return render_template('register.htm', title='Register', form=form)


# Use this endpoint to change password
@admin.route('/change_password/', methods=['GET', 'POST'])
def change_password():
    if not current_user.is_authenticated:
        admin_only_msg = "Sorry, only users can change their passwords."
        flash(admin_only_msg)
        return render_template('change_password.htm', title='Change Password', admin_only_msg=admin_only_msg)
    form = ChangePasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.password.data)
        db.session.commit()
        flash('Password changed')
        return redirect(url_for('.login'))
    return render_template('change_password.htm', title='Change Password', form=form)

# TODO: change register to add username/email only, and then check in login if user has a password.
# TODO: If they don't have a password prompt them to create one (so we can continue w/ the execs add other execs paradigm)
