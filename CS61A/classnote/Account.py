class Account:
    def __init__(self, holder):
        self.balance = 0
        self.holder = holder

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            print("broke")
            return "Broke"
        self.balance -= amount
        print(self.balance)
        return self.balance

