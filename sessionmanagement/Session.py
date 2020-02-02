from sessionmanagement import RedisInit
import uuid


class Session(RedisInit.RedisInit):
    def __init__(self, session_key=None, username=None):
        super().__init__()
        self.session_key = session_key
        self.username = username

    def confirm_session(self):
        val = super().match_sess_key(self.session_key)
        if val:
            return val
        return self.create_session()

    def create_session(self):
        self.generate_session_key()
        super().add_key_value(self.session_key, self.username)
        if not self.confirm_session():
            return False
        return True

    def delete_session(self):
        pass

    def generate_session_key(self):
        self.session_key = str(uuid.uuid4())
