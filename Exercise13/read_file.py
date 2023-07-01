

# 6 Use a loop to iterate over and print the contents of the file. Do not to include any blank lines in the output.

with open('pelican.txt') as x:
    f = x.read()

print("the type of data is ", type(f))

print("")
print("")

print(f)

print("")
print("")

# What data type is the output?
print("the type of data is ", type(f))

pelican_list = open("pelican.txt").readlines()

print("")
print("")

print(type(pelican_list))
print("There are ", len(pelican_list), " items in this list")

print("")
print("")

with open("pelican.txt") as p:
    for line in p:
        print(line.strip())
