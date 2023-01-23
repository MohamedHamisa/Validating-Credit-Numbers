# importing the regular expression module
import re

# compile the patterns
pattern = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}'
    r'(?:-?\d{4}){3}'
    r'$')

# using for loop to the input from user 
for _ in range(int(input().strip())):
    
    #using pattern to search if the number is valid
    print('Valid' if pattern.search(input().strip()) else 'Invalid')

'''
It must start with a 4, 5 or 6.
It must contain exactly 16 digits.
It must only consist of digits (0-9).
It may have digits in groups of 4, separated by one hyphen “-“.
It must NOT use any other separator like ' ' , '_', etc.
'''


