from flask_login import UserMixin, AnonymousUser

class User(UserMixin):

    def __init__(self, name, id, active=True):
        self.name = name

    def is_active(self):
        return self.active

class Anonymous(AnonymousUser):
    name = u"Anonymous"