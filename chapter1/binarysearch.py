
"""
This script implements a binary search algorithm.
Functions:
    binary_search(list, item): Searches for an item in a sorted list using the binary search algorithm.
Example usage:
    print(binary_search(list, 3))  # Output: 1
    print(binary_search(list, -1)) # Output: None
    print(binary_search(list, 9))  # Output: 4
"""

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

list = [1, 3, 5, 7, 9]
print(binary_search(list, 3)) # => 1
print(binary_search(list, -1)) # => None
print(binary_search(list, 9)) # => 4