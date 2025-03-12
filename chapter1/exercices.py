# 1.2 Suppose you have a sorted list of 128 names, and you’re searching 
# through it using binary search. What’s the maximum number of 
# steps it would take?

import math

def max_steps_binary_search(n):
    return math.ceil(math.log2(n))

# Number of names in the list
num_names = 128

# Calculate the maximum number of steps
max_steps = max_steps_binary_search(num_names)

print(f"The maximum number of steps it would take to search through a list of {num_names} names using binary search is {max_steps}.")

# Output
# The maximum number of steps it would take to search through a list of 128 names using binary search is 7.


# Suppose you double the size of the list
num_names_doubled = num_names * 2

# Calculate the maximum number of steps for the doubled list
max_steps_doubled = max_steps_binary_search(num_names_doubled)

print(f"The maximum number of steps it would take to search through a list of {num_names_doubled} names using binary search is {max_steps_doubled}.")

# Output
# The maximum number of steps it would take to search through a list of 256 names using binary search is 8.

# 1.3 You have a name, and you want to find the person’s phone number in the phone book.

# The runtime for binary search is O(log n), where n is the number of entries in the phone book.

# Example:
phone_book_size = 1000  # Suppose the phone book has 1000 entries

# Calculate the maximum number of steps for binary search in the phone book
max_steps_phone_book = max_steps_binary_search(phone_book_size)

print(f"The maximum number of steps it would take to find a person's phone number in a phone book of {phone_book_size} entries using binary search is {max_steps_phone_book}.")

# Output
# The maximum number of steps it would take to find a person's phone number in a phone book of 1000 entries using binary search is 10.

# 1.4 You have a phone number, and you want to find the person’s name in the phone book.
# The runtime for a linear search is O(n), where n is the number of entries in the phone book.

# Calculate the maximum number of steps for linear search in the phone book
max_steps_linear_search = phone_book_size

print(f"The maximum number of steps it would take to find a person's name in a phone book of {phone_book_size} entries using linear search is {max_steps_linear_search}.")

# Output
# The maximum number of steps it would take to find a person's name in a phone book of 1000 entries using linear search is 1000.


# 1.5 You want to read the numbers of every person in the phone book.
# The runtime for reading all entries is O(n), where n is the number of entries in the phone book.

# Calculate the maximum number of steps for reading all entries in the phone book
max_steps_read_all = phone_book_size

print(f"The maximum number of steps it would take to read the numbers of every person in a phone book of {phone_book_size} entries is {max_steps_read_all}.")

# Output
# The maximum number of steps it would take to read the numbers of every person in a phone book of 1000 entries is 1000.
