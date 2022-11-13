#
from class_c import Human


class Superhero(Human):
    # redefine
    species = "Superhuman"

    def __init__(self, name, movie=False, superpowers=['light', 'fire']):
        # run father class's construct function
        super().__init__(name)
        self.movie = movie
        self.superpowers = superpowers

    # reconstruct sing
    def sing(self):
        return 'Dun Dun'

    # new method
    def boast(self):
        for power in self.superpowers:
            print("ah...{pow}".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="hulk")

    if isinstance(sup, Human):
        print('I am human')
    if type(sup) is Superhero:
        print('I am a hero')

    # get Mro
    print(Superhero.__mro__)

    # father's method, own value
    sup.say(sup.get_species())

    # call redefine function
    sup.say(sup.sing())

    # call SuperHero method
    sup.boast()

    # superhero's value
    print("Oscar?" + str(sup.movie))