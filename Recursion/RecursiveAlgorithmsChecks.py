
# R-4.1

"""
To find the maximum element in a sequence S of n elements recursively, you can follow these steps:

Base case: If the sequence S contains only one element, return that element as the maximum.

Recursive case:

Divide the sequence S into two halves: S1 and S2.
Recursively find the maximum element in each half by calling the same algorithm.
Compare the maximum elements found in the two halves.
Return the larger of the two maximum elements as the maximum for the entire sequence S.
"""


def find_max(S):
    n = len(S)

    if n == 1:
        return S[0]  # Base case: Only one element in the sequence

    # Divide the sequence into two halves
    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]

    # Recursive calls
    max1 = find_max(S1)  # Find the maximum element in S1
    max2 = find_max(S2)  # Find the maximum element in S2

    # Compare the maximum elements found in the two halves
    if max1 > max2:
        return max1
    else:
        return max2



# -----------------------------------------------------------

# R-4.2  (solution in notebook)

"""
power(2, 5)
  |
  |-- power(2, 4)
  |   |
  |   |-- power(2, 3)
  |   |   |
  |   |   |-- power(2, 2)
  |   |   |   |
  |   |   |   |-- power(2, 1)
  |   |   |   |   |
  |   |   |   |   |-- power(2, 0)
  |   |   |   |   |   |
  |   |   |   |   |   |-- return 1
  |   |   |   |   |
  |   |   |   |   |-- return 2 * 1 = 2
  |   |   |   |
  |   |   |   |-- return 2 * 2 = 4
  |   |   |
  |   |   |-- return 2 * 4 = 8
  |   |
  |   |-- return 2 * 8 = 16
  |
  |-- return 2 * 16 = 32

"""

# -------------------------------------------------------------------------------------------------------------

# C-4.9


def find_min_max(sequence):
    if len(sequence) == 1:
        return sequence[0], sequence[0]  # Base case: Only one element in the sequence
    else:
        mid = len(sequence) // 2
        left_min, left_max = find_min_max(sequence[:mid])  # Recursive call for the left half
        right_min, right_max = find_min_max(sequence[mid:])  # Recursive call for the right half
        return min(left_min, right_min), max(left_max, right_max)  # Combine the results


"""
This function uses the concept of divide and conquer. It recursively divides the sequence into halves until it reaches 
the base case of having only one element. Then, it combines the minimum and maximum values obtained from the left and 
right halves. Finally, it returns the overall minimum and maximum values of the sequence.

You can call this function with your sequence as an argument, like find_min_max([5, 2, 9, 1, 7]), and it will return a 
tuple containing the minimum and maximum values (1, 9).
"""

# ---------------------------------------------------------------------------------------------------------------

# C-4.17


def is_palindrome(s):
    if len(s) <= 1:
        return True  # Base case: Empty string or string with one character is a palindrome
    else:
        first = s[0]
        last = s[-1]
        if first == last:
            return is_palindrome(s[1:-1])  # Recursive call with the substring excluding the first and last characters
        else:
            return False


"""
This function checks if the first and last characters of the string s are equal. If they are, it recursively calls 
itself with the substring obtained by excluding the first and last characters. This process continues until the base 
case is reached, where an empty string or a string with one character is considered a palindrome. If at any point the 
first and last characters are not equal, the function returns False. Otherwise, if the function completes all recursive 
calls without returning False, it means that the string is a palindrome, and it returns True.

You can call this function with your string as an argument, like is_palindrome("racecar"), and it will return True.
"""