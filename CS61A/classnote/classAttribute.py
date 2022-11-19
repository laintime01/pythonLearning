class Fruit:
    weight = 0.1

    def __init__(self, color):
        self.color = color


apple = Fruit('red')
apple.weight = 0.2
print(Fruit.weight)
Fruit.weight = 0.4
print(apple.weight)
pitch = Fruit('yellow')
print(pitch.weight)
