# Function to reverse a string
from math import factorial


def reverse_string(s):
    # Reverse the string using reversed() and join() methods.
    # reversed(s) returns an iterator; ''.join() concatenates the characters into a string.
    return ''.join(reversed(s))

# Test 1. Verification of reverse_string function
# Positive test
def test_reverse_string():
    # Define the input string
    input_str = "TripleTen"
    # Perform the reverse operation
    reversed_str = reverse_string(input_str)
    # Check if the reversed string matches the expected output
    assert reversed_str == "neTelpirT"
    print("Test Passed! " + input_str + "'s reverse is " + reversed_str)




def is_palindrome(s):
    # Reverse the string using reversed() and join() methods.
    reversed_str = ''.join(reversed(s))
    # Check if the reversed string is equal to the original string
    return s == reversed_str

# Test 2. Verification of is_palindrome function
def test_is_palindrome():
    # Define the input string
    input_str = "racecar"
    # Perform the palindrome check
    result = is_palindrome(input_str)
    # Check if the result is True for a palindrome
    assert result == True
    print("Test Passed! '" + input_str + "' is a palindrome.")

def compute_factorial(n):
    # Compute the factorial of n using Python's built-in factorial function from the math module.
    return factorial(n)

# Test 1. Verification of compute_factorial function
def test_compute_factorial():
    # Define the input number
    input_number = 5
    # Perform the factorial computation
    result = compute_factorial(input_number)
    # Check if the result is equal to the expected factorial value
    assert result == 120
    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))


# Function to check anagram
def are_anagrams(string1, string2):
    # Check if two strings are anagrams by sorting and comparing them.
    return sorted(string1) == sorted(string2)


# Test 4. Verification of are_anagrams function
def test_are_anagrams():
    # Define the input strings
    word_string1 = "listen"
    word_string2 = "silent"

    # Perform the anagram check
    result = are_anagrams(word_string1, word_string2)

    # Check if the result is True for anagrams
    assert result == True

    print("Test Passed! '" + word_string1 + "' and '" + word_string2 + "' are anagrams.")