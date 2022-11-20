class Car:
    num_wheels = 4
    gas = 30
    headlights = 2
    size = 'Tiny'

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.color = 'No color yet. You need to paint me.'
        self.wheels = Car.num_wheels
        self.gas = Car.gas

    def paint(self, color):
        self.color = color
        return self.make + ' ' + self.model + ' is now ' + color

    def drive(self):
        if self.wheels < Car.num_wheels or self.gas <= 0:
            return 'Cannot drive!'
        self.gas -= 10
        return self.make + ' ' + self.model + ' goes vroom!'

    def pop_tire(self):
        if self.wheels > 0:
            self.wheels -= 1

    def fill_gas(self):
        self.gas += 20
        return 'Gas level: ' + str(self.gas)


# sup class
class MonsterTruck(Car):
    size = 'Monster'

    def rev(self):
        print('Vroom! This Monster Truck is huge!')

    def drive(self):
        self.rev()
        return super().drive()


deneros_car = Car('Tesla', 'Model S')
print(deneros_car.model)
deneros_car.gas = 10  # Model S
print(deneros_car.drive())  # Tesla Model S goes vroom
print(deneros_car.drive())  # Cannot drive
print(deneros_car.fill_gas())  # Gas level: 20
print(deneros_car.gas)  # 20
print(Car.gas)  # 30
deneros_car.wheels = 2
print(deneros_car.wheels)  # 2
print(Car.num_wheels)  # 4
print(deneros_car.drive())  # Cannot drive
# print(Car.drive()) # error
print(Car.drive(deneros_car))  # Cannot drive

deneros_car = MonsterTruck('Monster', 'Batmobile')
print(deneros_car.drive())
print(MonsterTruck.drive(deneros_car))


# print(Car.rev(deneros_car)) # error

# Q2
class Account:
    """An account has a balance and a holder.
    >>> a = Account('John')
    >>> a.deposit(10)
    10
    >>> a.balance
    10
    >>> a.interest
    0.02
    >>> a.time_to_retire(10.25) # 10 -> 10.2 -> 10.404
    2
    >>> a.balance               # balance should not change
    10
    >>> a.time_to_retire(11)    # 10 -> 10.2 -> ... -> 11.040808032
    5
    >>> a.time_to_retire(100)
    117
    """
    max_withdrawal = 10
    interest = 0.02

    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        if amount > self.max_withdrawal:
            return "Can't withdraw that amount"
        self.balance = self.balance - amount
        return self.balance

    def time_to_retire(self, amount):
        """Return the number of years until balance would grow to amount"""
        assert self.balance > 0 and amount > 0 and self.interest > 0
        ans = 0
        future = self.balance
        while future < amount:
            future += future * self.interest
            ans += 1
        return ans


# Q3
class FreeChecking(Account):
    """A bank account that charges for withdrawals, but the first two are free!
    >>> ch = FreeChecking('Jack')
    >>> ch.balance = 20
    >>> ch.withdraw(100)  # First one's free. Still counts as a free withdrawal even though it was unsuccessful
    'Insufficient funds'
    >>> ch.withdraw(3)    # Second withdrawal is also free
    17
    >>> ch.balance
    17
    >>> ch.withdraw(3)    # Ok, two free withdrawals is enough
    13
    >>> ch.withdraw(3)
    9
    >>> ch2 = FreeChecking('John')
    >>> ch2.balance = 10
    >>> ch2.withdraw(3) # No fee
    7
    >>> ch.withdraw(3)  # ch still charges a fee
    5
    >>> ch.withdraw(5)  # Not enough to cover fee + withdraw
    'Insufficient funds'
    """
    withdraw_fee = 1
    free_withdrawals = 2
    def __init__(self, account_holder):
        super().__init__(account_holder)
        self.withdraws = 0

    def withdraw(self, amount):
        self.withdraws += 1
        fee = 0
        if self.withdraws > self.free_withdrawals:
            fee = self.withdraw_fee
        return super().withdraw(amount + fee)




