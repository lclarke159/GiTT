# Instruction for where to find python
#! /usr/bin/python

# Example Python Script
import sys


# argc variable that stores the number of inputs to the programme
argument_count = len(sys.argv)
# Checks how many arguments if more than 1 will print "too many..."
# IF is a conditional operator
if argument_count > 1:
    print('Too many args')
else:
    # assign World to variable 'where'
    where = 'World'
    print("Hello", where)

# will print goodbye from [name of file] regardless of if / else statement as not indented.
print('Goodbye from ' + sys.argv[0])

# print(sys.argv[3])
