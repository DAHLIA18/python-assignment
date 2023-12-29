def print_odd_indices(lst):
    for i in range(len(lst)):
        if i % 2 != 0:
            print(lst[i])


def test_print_odd_indices_empty_list():
    captured_output = []
    print_odd_indices([])
    assert captured_output == [], "Empty list should not print anything"

def test_print_odd_indices_numbers():
    captured_output = []
    print_odd_indices([1, 2, 3, 4, 5])
    assert captured_output == [2, 4], "Odd indices: 2, 4"

def test_print_odd_indices_strings():
    captured_output = []
    print_odd_indices(['apple', 'banana', 'orange', 'pear'])
    assert captured_output == ['banana', 'pear'], "Odd indices: 'banana', 'pear

test_print_odd_indices_empty_list()
test_print_odd_indices_numbers()
test_print_odd_indices_strings()
