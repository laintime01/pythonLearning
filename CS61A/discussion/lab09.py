# Q1 Subsequences
def insert_into_all(item, nested_list):
    """Return a new list consisting of all the lists in nested_list
    >>> n1 = [[], [1,2], [3]]
    >>> insert_into_all(0, n1)
    [[0], [0, 1, 2], [0, 3]]
    """
    return [[item] + lst[:] for lst in nested_list]


def subseqs(s):
    """Return a nested list of all subsequences of S
    >>> seqs = subseqs([1, 2, 3])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
    >>> subseqs([])
    [[]]
    """
    if not s:
        return [[]]
    else:
        subset = subseqs(s[1:])
        return insert_into_all(s[0], subset) + subset


# Q2 Non-Decreasing subsequences
def non_sub(s):
    """Return a nested list of all subsequences of S that
    elements are non-decreasing
    >>> seqs = non_sub([1,3,2])
    >>> sorted(seqs)
    [[], [1], [1, 2], [1, 3], [2], [3]]
    >>> non_sub([])
    [[]]
    """

    def subseq_helper(s, prev):
        if not s:
            return [[]]
        elif s[0] < prev:
            return subseq_helper(s[1:], prev)
        else:
            a = subseq_helper(s[1:], s[0])
            b = subseq_helper(s[1:], prev)
            return insert_into_all(s[0], a) + b

    return subseq_helper(s, 0)


# Q3 number of trees
def num_trees(n):
    """return number of trees
    >>> num_trees(1)
    1
    >>> num_trees(2)
    1
    >>> num_trees(3)
    2
    >>> num_trees(8)
    429
    """
    if n == 1:
        return 1
    return sum(num_trees(k) * num_trees(n - k) for k in range(1, n))


# Q4 partition generator
def partition_gen(n):
    def yield_helper(j, k):
        if j == 0:
            yield []
        elif k > 0 and j > 0:
            for small_part in yield_helper(j - k, k):
                yield [k] + small_part
            yield from yield_helper(j, k - 1)

    yield from yield_helper(n, n)


# Q5 Vending machine
class VendingMachine:
    """A vending machine that vends some product for some price
    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock'
    >>> v.addfunds(15)
    'Nothing left to vend. Please restock, Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please update your balance with $10 more funds.'
    >>> v.addfunds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please update your balance with $3 more funds.'
    >>> v.addfunds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change'
    >>> v.addfunds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'


    """

    def __init__(self, product, price):
        self.product = product
        self.price = price
        self.stock = 0
        self.fund = 0

    def vend(self):
        if self.stock == 0:
            return 'Nothing left to vend. Please restock'
        elif self.price > self.fund:
            return f'Please update your balance with ${self.price - self.fund} more funds.'
        elif self.price == self.fund:
            self.stock -= 1
            self.fund = 0
            return 'Here is your candy.'
        else:
            diff = self.fund - self.price
            self.stock -= 1
            self.fund = 0
            return f'Here is your candy and ${diff} change'

    def addfunds(self, n):
        if self.stock == 0:
            return f'Nothing left to vend. Please restock, Here is your ${n}.'
        else:
            self.fund += n
            return f'Current balance: ${self.fund}'

    def restock(self, n):
        self.stock += n
        return f'Current candy stock: {self.stock}'


# Q6 Trade
def trade(first, second):
    m, n = 1, 1
    equal_prefix = lambda: sum(first[:m]) == sum(second[:n])
    while m <= len(first) and n <= len(second) and not equal_prefix():
        if sum(first[:m]) < sum(second[:n]):
            m += 1
        else:
            n += 1
    if equal_prefix():
        first[:m], second[:n] = second[:n], first[:m]
        return 'Deal'
    return 'No Deal'


# Q7 shuffle
def card(n):
    """Return the card numeral as a string for a positive n <= 13."""
    assert type(n) == int and 0 < n <= 13, 'Bad card n'
    specials = {1: 'A', 11: 'J', 12: 'Q', 13: 'K'}
    return specials.get(n, str(n))


def shuffle(cards):
    """Return a shuffled list that interleaves the two halves of cards
    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> suits = ['H', 'D', 'S', 'C']
    """
    assert len(cards) % 2 ==0, 'len(cards) must be even'
    half = len(cards) // 2
    shuffled = []
    for i in range(half):
        shuffled.append(cards[i])
        shuffled.append(cards[half+i])
    return shuffled