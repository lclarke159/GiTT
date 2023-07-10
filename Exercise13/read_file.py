
# Use the open and read methods to slurp the entire contents of your
# pelican.txt file.
with open('pelican.txt') as x:
    f = x.read()

# Display the type of the returned data and print the contents of the
# returned data.
print("the type of data is ", type(f))

print("")
print("")

print(f)

print("")
print("")

# What data type is the output?
print("the type of data is ", type(f))

# Now, write some code that will read the pelican.txt file into a list and
# then output the number of items within the list.
pelican_list = open("pelican.txt").readlines()

print("")
print("")

print(type(pelican_list))
print("There are ", len(pelican_list), " items in this list")

print("")
print("")

# Now use a loop to iterate over and print the contents of the file. Be sure
# not to include any blank lines in the output.
with open("pelican.txt") as p:
    for line in p:
        if len(line) > 1:
            print(line.strip())
