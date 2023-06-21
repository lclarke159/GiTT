#!/usr/bin/python

Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print("")
print("Same number of hyphens as the original string:")
print("")
# Get the length of the string
belgium_length = len(Belgium)
# Print the same number of hyphens as the string
belgium_hyphens = "-" * belgium_length
print(belgium_hyphens)


# Replace commas with colons
print("")
print("Commas have been replaced with colons")
print("")
belgium_colon = Belgium.replace(',', ':')
print(belgium_colon)

# The population of Belgium (the second field), plus the population
# of the capital city (the fourth field). Hint: the answer should be
# 11183818.
print("")
print("Population of Belgium plus population of Capital")
print("")

# Split list using where there are commas
belgium_list = Belgium.split(",")

# Get first figure in list at place 2 (1 due to counting from 0)
# Convert to int so we can add
belgium_population = int(belgium_list[1])
# Get second figure in list at place 4 (3 due to counting from 0)
# Convert to int so we can add
capital_population = int(belgium_list[3])

total_population = belgium_population + capital_population
print(total_population)

