def running_total(lst):
    total = 0
    result = []
    for num in lst:
        total += num
        result.append(total)
    return result


def test_running_total_empty_list():
    result = running_total([])
    assert result == [], "Running total of an empty list should be an empty list"

def test_running_total_numbers():
    result = running_total([1, 2, 3, 4, 5])
    assert result == [1, 3, 6, 10, 15], "Running total of [1, 2, 3, 4, 5] should be [1, 3, 6, 10, 15]"

def test_running_total_negative_numbers():
    result = running_total([-1, -2, -3, -4, -5])
    assert result == [-1, -3, -6, -10, -15], "Running total of [-1, -2, -3, -4, -5] should be [-1, -3, -6, -10, -15]"


test_running_total_empty_list()
test_running_total_numbers()
test_running_total_negative_numbers()
