import redis


class RedisInit:
    def __init__(self):
        self.pool = redis.ConnectionPool(host='localhost', port=6379, db=0)

    @property
    def conn(self):
        return redis.Redis(connection_pool=self.pool)

    def add_key_value(self, key, value, ex=None, px=None, nx=False, xx=False):
        """
        :param key: Key to add
        :param value: Value to add to the key
        :param ex: expiry in seconds
        :param px: expiry in milliseconds
        :param nx: if this is set to True, it will only set the value at key if it doesn't exist
        :param xx: if this is set to True, it will only set the value at key if it does exist
        :return:
        """
        try:
            self.conn.set(key, value)
        except redis.RedisError as e:
            raise e

    def del_keys(self, *keys):
        return self.conn.delete(*keys)

    def change_val(self, key, value):
        """
        getset(key, value) returns the old value at KEY. We can use this to confirm to the user it has changed
        """
        return self.conn.getset(key, value)

    def match_sess_key(self, sess_key):
        for key in self.conn.scan_iter(match=sess_key):
            if key:
                return True
        return False

    def get_key_value(self, key):
        """
        this doesnt work as of yet... this will just return the key
        :param key:
        :return:
        """
        return self.conn.get(key.decode('utf-8'))

    def get_values(self, value):
        pass

    def rename_key(self, key, new_key):
        return self.conn.rename(key, new_key)

    def sort(self):
        pass

    def get_keys(self):
        keys = [k.decode('utf-8') for k in self.conn.scan_iter(match='*')]
        return keys

    def clear_db(self):
        for key in self.conn.scan_iter(match='*'):
            self.conn.delete(key)
