from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,\
    BooleanField, SubmitField,\
    SelectField, TextAreaField,\
    DateTimeField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.util.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class ProjectForm(FlaskForm):
    id = 'project'
    project_title = StringField('Project Title', validators=[DataRequired()])
    project_text = TextAreaField('Project Description', validators=[DataRequired()])
    project_tags = TextAreaField('Project Tags')

    submit = SubmitField('Submit Project')

class TeamMemberForm(FlaskForm):
    id = 'team_member'
    team_name = StringField('Team Name', validators=[DataRequired()])
    team_member_name = StringField('Member Name', validators=[DataRequired()])
    team_member_email = StringField('Email', validators=[DataRequired()])

    submit = SubmitField('Submit Team Member')

class ExecMemberForm(FlaskForm):
    id = 'executive'
    exec_team = StringField('Exec Team (BD, Ops, Marketing, etc.)', validators=[DataRequired()])
    exec_member_name = StringField('Member Name', validators=[DataRequired()])
    exec_member_email = StringField('Email', validators=[DataRequired()])

    submit = SubmitField('Submit Exec Member')

class EventForm(FlaskForm):
    id = 'event'
    event_title = StringField('Event Title', validators=[DataRequired()])
    event_date = DateTimeField('Event Date', validators=[DataRequired()])
    # TODO possibly use a google maps API here to link directly to maps
    event_location = StringField('Event Location', validators=[DataRequired()])
    event_desc = TextAreaField('Event Description', validators=[DataRequired()])

    submit = SubmitField('Submit EventForm')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class ContactUsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired("Please enter your name.")])
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    subject = StringField('Subject', validators=[DataRequired("Please enter a subject.")])
    message_text = TextAreaField('Email Body', validators=[DataRequired("Please enter a message.")])

    submit = SubmitField('Submit Email')