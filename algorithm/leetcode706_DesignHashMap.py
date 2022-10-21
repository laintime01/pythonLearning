class MyHashMap(object):
    def __init__(self):
        self.dict = {}

    def put(self, key, value):
        self.dict[key] = value

    def get(self, key):
        if key in self.dict:
            return self.dict[key]
        return -1

    def remove(self, key):
        if key in self.dict:
            self.dict.pop(key)