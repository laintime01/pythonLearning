# design a simple hashset with add remove and contain function
class MyHashSet(object):
    def __init__(self):
        self.set = [False] * 1000001

    def add(self, key):
        self.set[key] = True

    def remove(self, key):
        self.set[key] = False

    def contains(self, key):
        return self.set[key]


ms = MyHashSet()
print(ms.add(2))
print(ms.contains(2))
print(ms.add(1))
print(ms.contains(1))
print(ms.remove(1))
print(ms.contains(1))
