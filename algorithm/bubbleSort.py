def magic_bubble_sort(numbers):
    """ magic bubble sort, all even are bigger than odd numbers
    :param numbers: List[int]
    :return: List[int]
    """
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i+1]
            current_is_even, next_is_even = numbers[i] % 2 == 0, numbers[i+1] % 2 == 0
            should_swap = False
            # current and next both even or odd, but current is bigger
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True

            if should_swap:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers
