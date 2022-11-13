# class
class Human:
    # class value
    species = "H. sapiens"

    # init function will be called when instance is created
    def __init__(self, name):
        self.name = name

        # init value
        self._age = 0

    # method, first always self which is the instance itself
    def say(self, msg):
        print('{name}:{message}'.format(name=self.name, message=msg))

    def sing(self):
        return 'yo...yo..'

    # class method will be used by all instance of this class
    @classmethod
    def get_species(cls):
        return cls.species

    # static method, has no bound with instance or class
    @staticmethod
    def grunt():
        return "*grunt*"

    # property, like getter
    @property
    def age(self):
        return self._age

    # could be changed
    @age.setter
    def age(self, age):
        self._age = age

    # could be deleted
    @age.deleter
    def age(self):
        del self._age


# when python interpreter read source code, it will run all code in the file
# check __name__ could make it only be run when this is the main(not in import)
if __name__ == '__main__':
    i = Human(name='messi')
    i.say('hi')
    j = Human(name='C7')
    j.say('siu')

    # class method
    i.say(i.get_species())
    # change shared value
    Human.species = "football player"
    i.say(i.get_species())
    j.say(j.get_species())
    # i and j both instance of human
    # run static method
    print(Human.grunt())
    j.say(j.grunt())
    # change instance value
    i.age = 37
    i.say(i.age)
    j.say(j.age)
    # delete value
    del i.age
    i.say(i.age) # AttributeError

