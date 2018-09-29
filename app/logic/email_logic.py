from app.util.string_literals import WEBSITE_PREFIX, SET_PASSWORD_EMAIL_STRING, BASEURL
from app import Config, mail
from flask_mail import Message
from flask import url_for

# Our config var for ADMINS in Heroku can only use Strings, so splitting them here to get list.
# Please only use a space as a delimiter.
admins = Config.ADMINS.split(' ')


def form_handler(form):
    message = Message(WEBSITE_PREFIX + form.subject.data, sender='operations@uoftveep.com', recipients=['operations@uoftveep.com'] + admins)
    message.body = """
    From: %s <%s>
    %s
    """ % (form.name.data, form.email.data, form.message_text.data)
    mail.send(message)


def send_set_password_email(email, username, password):
    message = Message(WEBSITE_PREFIX + "Set Your Admin Password", sender='operations@uoftveep.com', recipients=[email])
    message.body = SET_PASSWORD_EMAIL_STRING % (''.join([BASEURL, 'admin/login']), username, password, ''.join([BASEURL, 'admin/change_password']))
    mail.send(message)

# TODO rename functions to more descriptive names
