tup = 'Hello'
print(len(tup))
tup = 'Hello',
print(len(tup))
# the comma transforms this string in to a list with 1 item as a comma is used to separate items in a list or tuple.
# When a string ends with a comma, it is interpreted as a list with one item (adding 'Goodbye' would return 2)
# The length returned is 1 (item) rather than 5 characters.
tup = 'Hello', 'Goodbye'
print("The length is now ", len(tup))
