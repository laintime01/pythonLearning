# Q1 Num eights
def num_eights(pos):
    """returns the number of times 8 appears as a digit of pos
    >>> num_eights(3)
    0
    >>> num_eights(888112)
    3
    >>> num_eights(12345)
    0
    """
    # loop
    # count,i,pos = 0,0,str(pos)
    # while i < len(pos):
    #     if pos[i:i+1] == "8":
    #         count +=1
    #     i += 1
    # return count
    # recursion
    if pos % 10 == 8:
        return 1 + num_eights(pos // 10)
    elif pos < 10:
        return 0
    else:
        return num_eights(pos // 10)


# Q2 Ping-pong
def pingpong(n):
    """implement a function pingpong that
     returns the nth element of the ping-pong sequence
     >>> pingpong(8)
     8
     >>> pingpong(10)
     6
     >>> pingpong(15)
     1
     >>> pingpong(22)
     -2
     >>> pingpong(69)
     -1
     """

    def steps(result, i, step):
        if i == n:
            return result
        elif i % 8 == 0 or num_eights(i) > 0:
            return steps(result - step, i + 1, -step)
        else:
            return steps(result + step, i + 1, step)

    return steps(1, 1, 1)


# Q3 Count coins

def next_larger_coin(coin):
    """return next larger coin in order"""
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def next_smaller_coin(coin):
    """return next smaller coin in order"""
    if coin == 25:
        return 10
    elif coin == 10:
        return 2
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value 1,5,10,25
    >>> count_coins_again(15)
    6
    >>> count_coins_again(10)
    4
    >>> count_coins_again(20)
    9
    """
    def count_changes(change, largest_coin):
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif largest_coin is None:
            return 0
        else:
            with_coin = count_changes(change - largest_coin, largest_coin)
            without_coin = count_changes(change, next_smaller_coin(largest_coin))
        return without_coin + with_coin

    return count_changes(change, 25)


# alternative solution
def count_coins_again(change):
    """try another solution
    >>> count_coins_again(15)
    6
    >>> count_coins_again(10)
    4
    >>> count_coins_again(20)
    9
    """
    def count_coins_again(change, smallest):
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif smallest is None:
            return 0
        else:
            with_coin = count_coins_again(change-smallest, smallest)
            without_coin = count_coins_again(change, next_larger_coin(smallest))
        return without_coin + with_coin
    return count_coins_again(change, 1)
