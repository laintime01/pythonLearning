def enume(y):
    """
    >>> enume([7, 8, 3])
    0 7
    1 8
    2 3
    """
    for index, ele in enumerate(y):
        print(index, ele)


# minimum
def find_min(y):
    """
    >>> y = 'bug'
    >>> find_min(y)
    'b'
    """
    return min(y)


# add managed attributes to classes
import hashlib
import os


class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
    # good way to use class property
    @property
    def password(self):
        raise AttributeError('Password is write-only')

    @password.setter
    def password(self, plaintext):
        salt = os.urandom(32)
        self._hashed_password = hashlib.pbkdf2_hmac('sha256', plaintext.encode('utf-8'),
                                                    salt, 100_100)
