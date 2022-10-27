def findBig(list):
    """
    :param list: int list
    :return: int
    """
    if not list:
        return None
    if len(list) == 1:
        return list[0]
    elif len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    find_sub_list = findBig(list[1:])
    return list[0] if list[0] > find_sub_list else find_sub_list


# test
list0 = [2,9]
list1 = [1, 4, 7, 8, 2]
print(findBig(list0))
print(findBig(list1))
# print(max(list0))
