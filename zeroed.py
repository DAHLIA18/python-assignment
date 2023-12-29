def zeroed_code(numbers):
    if len(numbers) >= 1:
        numbers[0] = 0  # Zero the first number
    if len(numbers) >= 2:
        numbers[-1] = 0  # Zero the last number
    return numbers

test1 = [1, 2, 3, 4, 5]
result1 = zeroed_code(test1)
print(result1)

test2 = [9, 8, 7]
result2 = zeroed_code(test2)
print(result2)

test3 = [42]
result3 = zeroed_code(test3)
print(result3)

