
# Append the following line to the file using the write method of the file
# handle:
with open("pelican.txt", "w") as w:
    w.write("A wonderful bird is the pelican,")

# Append the following second line using the write method:
with open("pelican.txt", "a") as a:
    a.write("\nHis bill holds more than his belican.")

# Create a list of the following lines
lines = ["\nHe can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

# Append this list to the file using the writelines method.
with open("pelican.txt", "a") as a:
    a.writelines(lines)

# Why are the "\n" required?
# For new lines (special character / escape code)
