from sessionmanagement import RedisInit
import uuid


class Session(RedisInit.RedisInit):
    def __init__(self, session_key=None, username=None):
        super().__init__()
        self.session_key = session_key
        self.username = username

    def confirm_session(self):
        val = super().match_sess_key(self.username)
        if val:
            return val
        return self.create_session()

    def confirm_session_un(self):
        """
        function to confirm the session when the user logs in, just in case there is one. If there is, then we
        don't need to create one. If not, it continues and makes a new one
        """
        value = super().get_values(self.username)
        if value:
            return super().get_values(self.username)

        return self.create_session()

    def create_session(self):
        self.generate_session_key()
        super().add_key_value(self.username, self.session_key)
        if not self.confirm_session():
            return False
        return self.session_key

    def delete_session(self):
        pass

    def generate_session_key(self):
        self.session_key = str(uuid.uuid4())
