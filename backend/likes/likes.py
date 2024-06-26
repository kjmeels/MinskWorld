import json


class Like:
    def __init__(self, session, session_key="LIKE"):
        self._keys = None
        self.session = session
        self.session_key = session_key

    def add(self, pk):
        if pk in self.keys:
            raise ValueError("Объект уже существует.")
        else:
            self.keys.append(pk)
        self.update_session()

    def remove(self, pk):
        if int(pk) not in self.keys:
            raise ValueError("Такого объекта нет.")
        else:
            self.keys.remove(int(pk))
            self.update_session()

    def clear(self):
        self.keys = []
        self.update_session()

    def update_session(self):
        self.session[self.session_key] = self.serializable
        self.session.modified = True

    @property
    def keys(self):
        if self._keys is None:
            self._keys = json.loads(self.session.get(self.session_key, "[]"))
        return self._keys

    @keys.setter
    def keys(self, value):
        self._keys = value

    @property
    def serializable(self):
        return json.dumps(self.keys)

    @property
    def count(self):
        return len(self.keys)
