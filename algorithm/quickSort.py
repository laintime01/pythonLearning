def quickSort(nums):
    """
    :param nums: List[int]
    :return: List[int]
    """
    if len(nums) >= 2:
        mid = nums[len(nums) // 2]
        left_part, right_part = [],[]
        nums.remove(mid)
        for n in nums:
            if n < mid:
                left_part.append(n)
            else:
                right_part.append(n)
        return quickSort(left_part) + [mid] + quickSort(right_part)
    return nums


test_list = [26, 28, 11, 16,99,12,30,87]
print(quickSort(test_list))
