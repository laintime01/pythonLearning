# Bat
class Bat:
    species = 'Bat'

    def __init__(self, can_fly=True):
        self.can_fly = can_fly

    def say(self, msg):
        msg = '... ... ...'
        return msg

    # add new function
    def sonar(self):
        return ')))...((('


if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.can_fly)
