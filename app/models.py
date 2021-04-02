from app.const_and_app_enum.constants import Constants


class User(object):
    """This class represents a user for Flask login purpose"""

    def __init__(self, user_name):
        self.user_name = user_name

    def get_id(self):
        return self.user_name

    def set_user_logged(self, logged):
        self.logged = logged

    def is_active(self):
        return self.logged

    def is_authenticated(self):
        return True
