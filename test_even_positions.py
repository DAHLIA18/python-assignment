def print_even_positions(lst):
    for i in range(len(lst)):
        if i % 2 == 0:
            print(lst[i])


def test_print_even_positions_empty_list():
    captured_output = []
    print_even_positions([])
    assert captured_output == [], "Empty list should not print anything"

def test_print_even_positions_numbers():
    captured_output = []
    print_even_positions([1, 2, 3, 4, 5])
    assert captured_output == [1, 3, 5], "Even positions: 1, 3, 5"

def test_print_even_positions_strings():
    captured_output = []
    print_even_positions(['apple', 'banana', 'orange', 'pear'])
    assert captured_output == ['apple', 'orange'], "Even positions: 'apple', 'orange'"


test_print_even_positions_empty_list()
test_print_even_positions_numbers()
test_print_even_positions_strings()
