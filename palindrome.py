def is_palindrome(s):
    s = s.lower() 
    return s == s[::-1] 


def test_is_palindrome_empty_string():
    result = is_palindrome("")
    assert result == True, "Empty string should be considered a palindrome"

def test_is_palindrome_single_character():
    result = is_palindrome("a")
    assert result == True, "Single character should be considered a palindrome"

def test_is_palindrome_palindrome_string():
    result = is_palindrome("level")
    assert result == True, "'level' should be considered a palindrome"

def test_is_palindrome_non_palindrome_string():
    result = is_palindrome("hello")
    assert result == False, "'hello' should not be considered a palindrome"

def test_is_palindrome_case_insensitive():
    result = is_palindrome("Madam")
    assert result == True, "'Madam' (case-insensitive) should be considered a palindrome"


test_is_palindrome_empty_string()
test_is_palindrome_single_character()
test_is_palindrome_palindrome_string()
test_is_palindrome_non_palindrome_string()
test_is_palindrome_case_insensitive()
