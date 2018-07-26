from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.util.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SubmitInfoForm(FlaskForm):
    select = SelectField('Type',
                         choices=[('project', 'Project'), ('team_member', 'Team Member'), ('executive', 'Executive')],
                         default='Please select a field')

    # for select = Project
    project_title = StringField('Project Title', validators=[DataRequired])
    project_text = TextAreaField('Project Description', validators=[DataRequired])
    project_tags = TextAreaField('Project Tags')

    # for select = Team member
    team_name = StringField('Team Name', validators=[DataRequired])
    team_member_name = StringField('Member Name', validators=[DataRequired])
    team_member_email = StringField('Email', validators=[DataRequired])

    # for select = Executive
    exec_team = StringField('Exec Team (BD, Ops, Marketing, etc.)', validators=[DataRequired])
    exec_member_name = StringField('Member Name', validators=[DataRequired])
    exec_member_email = StringField('Email', validators=[DataRequired])

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