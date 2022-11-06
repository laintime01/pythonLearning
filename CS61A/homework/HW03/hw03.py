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
            return steps(result-step, i+1, -step)
        else:
            return steps(result+step, i+1, step)
    return steps(1, 1, 1)
