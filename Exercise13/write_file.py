

# 8. Run the script and confirm a new file called pelican.txt was created and
# that it contains the limerick as expected.

with open("pelican.txt", "w") as w:
    w.write("A wonderful bird is the pelican,")

with open("pelican.txt", "a") as a:
    a.write("\nHis bill holds more than his belican.")

lines = ["\nHe can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"]

with open("pelican.txt", "a") as a:
    a.writelines(lines)

# Why are the "\n" required?
# For new lines (special character / escape code)
