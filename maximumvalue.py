def maximum(value1, value2, value3):
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print(maximum(7,80,6))
print(maximum(65,4,70))
print(maximum(55,6,9)) 
