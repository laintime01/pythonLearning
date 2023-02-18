import functools
import time
from functools import update_wrapper, partial


class DelayedStart:
    """
    wait for a while before execution
    """

    def __init__(self, func, *, duration=1):
        update_wrapper(self, func)
        self.func = func
        self.duration = duration

    def __call__(self, *args, **kwargs):
        print(f'Wait for {self.duration} seconds before starting...')
        time.sleep(self.duration)
        return self.func(*args, **kwargs)

    def eager_call(self, *args, **kwargs):
        pass


def delayed_start(**kwargs):
    """
    decorator : delay some function's start
    """
    return partial(DelayedStart, **kwargs)

@delayed_start(duration=2)
def say_hello():
    print('hello world!')

say_hello()