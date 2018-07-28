from app import mail
from flask_mail import Message


def form_handler(form):
    message = Message(form.subject.data, sender='vincechou0311@gmail.com', recipients=['vin.chou@mail.utoronto.ca'])
    message.body = """
    From: %s <%s>
    %s
    """ % (form.name.data, form.email.data, form.message_text.data)
    mail.send(message)

