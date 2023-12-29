def check_duplicates(strings_list):
    seen = []
    duplicates = []
    
    for string in strings_list:
        if string in seen and string not in duplicates:
            duplicates.append(string)
        else:
            duplicates.seen(string)
    
    if duplicates:
        return duplicates
    else:
        return "No duplicates"

words = ["apple", "orange", "banana", "apple", "grape", "orange"]
result = words
print(result) 
