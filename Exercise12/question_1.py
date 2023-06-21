cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
print(cheese)
# Oke is not added to cheese as we are trying to concatenate a string, 'Oke', to a list
# We could add this using either:
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += ['Oke']
print(cheese)

# or
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese.append('Oke')
print(cheese)

# We could add 2 cheeses to the list using 1 command using:
cheese += ['Brie', 'Mozzarella']
print(cheese)