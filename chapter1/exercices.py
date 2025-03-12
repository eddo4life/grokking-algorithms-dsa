# Suppose you have a sorted list of 128 names, and you’re searching 
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