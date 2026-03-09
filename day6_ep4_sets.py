#Sets are values that are unordered and immutable - uses curly braces
#Used to remove duplicates and check for membership
cities = {'Nairobi', 'Mombasa', 'Kisumu', 'Nakuru', 'Eldoret', "Eldoret"}
print(cities)

#Check for membership
print('Nairobi' in cities)

#Check if different sets have similar values
capital_cities = {'Nairobi', 'Kisumu', 'Mombasa', 'Eldoret', 'Abuja', 'Jinja'}
print(capital_cities)
#Check what items are shared between the two sets
print(capital_cities.intersection(cities))
#Check what items are not shared between the two sets
print(capital_cities.difference(cities))

#Combine the two sets
print(capital_cities.union(cities))

#How to create an empty set
empty_set = set()
print(empty_set)