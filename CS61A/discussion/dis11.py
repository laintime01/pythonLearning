# Programs as Data
# Q1 If program python
def if_program(cond, true_, false_):
    """
    >>> eval(if_program("True", "3", "4"))
    3
    """
    return f"{true_} if {cond} else {false_}"
