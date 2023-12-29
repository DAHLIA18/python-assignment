def sum_with_for_loop(nums):
    total = 0
    for num in nums:
        total += num
    return total

def test_sum_with_for_loop_empty_list():
    result = sum_with_for_loop([])
    assert result == 0, "Sum of an empty list should be 0"

def test_sum_with_for_loop_positive_numbers():
    result = sum_with_for_loop([1, 2, 3, 4, 5])
    assert result == 15, "Sum of [1, 2, 3, 4, 5] should be 15"

def test_sum_with_for_loop_negative_numbers():
    result = sum_with_for_loop([-1, -2, -3, -4, -5])
    assert result == -15, "Sum of [-1, -2, -3, -4, -5] should be -15"


test_sum_with_for_loop_empty_list()
test_sum_with_for_loop_positive_numbers()
test_sum_with_for_loop_negative_numbers()
def sum_with_while_loop(nums):
    total = 0
    i = 0
    while i < len(nums):
        total += nums[i]
        i += 1
    return total

def test_sum_with_while_loop_empty_list():
    result = sum_with_while_loop([])
    assert result == 0, "Sum of an empty list should be 0"

def test_sum_with_while_loop_positive_numbers():
    result = sum_with_while_loop([1, 2, 3, 4, 5])
    assert result == 15, "Sum of [1, 2, 3, 4, 5] should be 15"

def test_sum_with_while_loop_negative_numbers():
    result = sum_with_while_loop([-1, -2, -3, -4, -5])
    assert result == -15, "Sum of [-1, -2, -3, -4, -5] should be -15

test_sum_with_while_loop_empty_list()
test_sum_with_while_loop_positive_numbers()
test_sum_with_while_loop_negative_numbers()
def sum_with_do_while_loop(nums):
    total = 0
    if len(nums) > 0:
        i = 0
        while True:
            total += nums[i]
            i += 1
            if i >= len(nums):
                break
    return total


def test_sum_with_do_while_loop_empty_list():
    result = sum_with_do_while_loop([])
    assert result == 0, "Sum of an empty list should be 0"

def test_sum_with_do_while_loop_positive_numbers():
    result = sum_with_do_while_loop([1, 2, 3, 4, 5])
    assert result == 15, "Sum of [1, 2, 3, 4, 5] should be 15"

def test_sum_with_do_while_loop_negative_numbers():
    result = sum_with_do_while_loop([-1, -2, -3, -4, -5])
    assert result == -15, "Sum of [-1, -2, -3, -4, -5] should be -15"


test_sum_with_do_while_loop_empty_list()
test_sum_with_do_while_loop_positive_numbers()
test_sum_with_do_while_loop_negative_numbers()





