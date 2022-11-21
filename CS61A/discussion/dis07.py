# Q2
class Email:
    """Every email object has 3 instance attributes:
    the message, the sender name, and the recipient name.
    >>> email = Email('hello', 'Alice', 'Bob')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Alice'
    >>> email.recipient_name
    'Bob'
    """

    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients"""

    def __init__(self):
        self.client = {}

    def send(self, mail):
        """Take an email and put it in the inbox of the client it is addressed to."""
        client = self.client[mail.recipient_name]
        client.receive(mail)

    def register_client(self, client, client_name):
        self.client[client_name] = client


class Client:
    """Each client has name, server and inbox
     >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """

    def __init__(self, server, name):
        self.server = server
        self.name = name
        self.inbox = []
        self.server.register_client(self, self.name)

    def compose(self, msg, receiver):
        email = Email(msg, self.name, receiver)
        self.server.send(email)

    def receive(self, msg):
        self.inbox.append(msg)

# Inheritance
class Pet:

    def __init__(self, name, owner):
        self.is_alive = True
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + " !")

    def talk(self):
        print(self.name)

class Dog(Pet):

    def talk(self):
        super().talk()
        print("This Dog says woof!")

    @classmethod
    def robo_factory(cls, owner):
        return cls('RoboDog', owner)

class Cat(Pet):
    def __init__(self, name, owner, lives=9):
        super().__init__(name,owner)
        self.lives = lives

    def talk(self):
        print(self.name + " says meow!")

    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.is_alive = False
        else:
            print("This cat has no more lives to lose")

    @classmethod
    def cat_creator(cls, owner):
        """Return a new instance of a cat
        >>> cat1 = Cat.cat_creator("Bryce")
        >>> isinstance(cat1, cat)
        True
        >>> cat1.owner
        'Bryce'
        >>> cat1.name
        "Bryce's Cat"
        """
        name = owner + "'s Cat"
        return cls(name, owner)

# Q4 NoistCat
class NoiseCat(Cat):
    """A cat repeat things twice"""
    def __init__(self, name, owner, lives=9):
        super().__init__(name, owner, lives) # not necessary

    def talk(self):
        """say things twice
        >>> NoiseCat('Magic', 'James').talk()
        Magic says meow !
        Magic says meow !
        """
        super().talk()
        super().talk()

# Q6 Repr-esentation

