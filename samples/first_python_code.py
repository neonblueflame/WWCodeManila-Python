# Basic example on how to print
# text using different approach in
# Python.

organization = 'Dark side!'

# You can print it right away!
print('Hello WomanWhoCode!')

# Example of string concatenation
print('Hello ' + organization)

# Using .format() function to attach a string
print('Hello {}'.format(organization))
# print(f'Hello {organization}')  # Can use this format with Python3.6

# First, replace the following text with your name
your_name = 'Darth Hanger'

# Then, uncomment the next line by removing the "#" sign
print('{} loves Python!'.format(your_name))

string = "Hanger"
print string
print len(string)
print string.upper()
print string.upper().isupper()
print string.lower()
print string.lower().islower()
print string[0]
string[0] = "P"
print string