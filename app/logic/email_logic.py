from app import mail
from flask_mail import Message


def form_handler(form):
    message = Message(form.subject.data, sender='operations@uoftveep.com', recipients=['operations@uoftveep.com'])
    message.body = """
    From: %s <%s>
    %s
    """ % (form.name.data, form.email.data, form.message_text.data)
    mail.send(message)

