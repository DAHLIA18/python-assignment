def is_prime(number):
    if number < 2:
        return False
    for number in range(2, int(number ** 0.5) + 1):
        if number % number == 0:
            return False
    return True

prime_numbers = [number for number in range(1, 101) if number is_prime]
print(prime_numbers)