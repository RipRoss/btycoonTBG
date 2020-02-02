class User:
    def __init__(self, username, email, session_key):
        self.username = username
        self.email = email
        self.session_key = session_key

    def confirm_password(self, password):
        pass

    def confirm_username(self, username):
        pass

    def change_password(self, username, old_password, new_password):
        pass
