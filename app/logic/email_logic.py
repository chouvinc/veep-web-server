from app import mail
from app.util.string_literals import WEBSITE_PREFIX, SET_PASSWORD_EMAIL_STRING
from flask_mail import Message
from flask import url_for

def form_handler(form):
    message = Message(WEBSITE_PREFIX + form.subject.data, sender='operations@uoftveep.com', recipients=['operations@uoftveep.com'])
    message.body = """
    From: %s <%s>
    %s
    """ % (form.name.data, form.email.data, form.message_text.data)
    mail.send(message)

def send_set_password_email(email):
    message = Message(WEBSITE_PREFIX + "Set Your Admin Password", sender='operations@uoftveep.com', recipients=[email])
    message.body = SET_PASSWORD_EMAIL_STRING % (url_for('admin.set_password'))
    mail.send(message)

# TODO rename functions to more descriptive names