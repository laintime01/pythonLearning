# function with behavior that varies over time
def make_withdraw_list(amount):
    a = [amount]

    def f(x):
        if a[0] - x < 0:
            return "Insufficient funds"
        a[0] -= x
        return a[0]

    return f


withdraw = make_withdraw_list(100)

print(withdraw(25))
print(withdraw(1000))
print(withdraw(10))
