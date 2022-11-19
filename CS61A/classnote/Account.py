class Account:
    interest = 0.02
    def __init__(self, holder):
        self.balance = 0
        self.holder = holder

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            return "Broke"
        self.balance -= amount
        return self.balance


# inheritance
class CheckingAccount(Account):
    interest = 0.01
    withdraw_free = 1

    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_free)


a = Account('John')
b = CheckingAccount('Tom')
print(a.balance, b.balance)
a.deposit(100)
b.deposit(100)
print(a.balance, b.balance)
a.withdraw(10)
b.withdraw(10)


class Bank:
    """A bank *has* accounts
    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    """

    def __init__(self):
        self.accounts = []

    def open_account(self, name, balance, type=Account):
        account = type(name)
        account.deposit(balance)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance*a.interest)

