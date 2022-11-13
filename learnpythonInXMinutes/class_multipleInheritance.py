# inheritatance from both bat and superHero
from class_Inheritance import Superhero
from bat import Bat

class Batman(Superhero, Bat):

    def __init__(self, *args,**kwargs):
        # *args **kwargs more clear
        Superhero.__init__(self, 'anonymous', movie=True,
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # redefine name
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nana na..Batman'

if __name__ == '__main__':
    bt = Batman()

    bt.say(Batman.__mro__)
    bt.say(bt.species)
    bt.say('I agree')
    bt.say(bt.sonar())

    # inherited class value
    bt.age = 100
    bt.say(bt.age)
