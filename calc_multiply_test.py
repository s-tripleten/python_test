def test_multiply():
    # Define the first number
    a = 2
    # Define the second number
    b = 3
    # Perform the multiplication operation
    multiply = a * b
    # Check if the user gets the expected
    assert multiply == 6


# Test 2. Verification of multiplication function
# Negative test

def test_multiply_neg():
    # Define the first number
    a = 3
    # Define the second number
    b = 3
    # Perform the multiplication operation
    multiply = a * b
    # Check if the user gets the expected
    assert multiply == 6

def reverse_string(s):
        # Create a reversed iterator
        reversed_string = reversed(s)

        # Return the iterator itself (not a string)
        return reversed_string