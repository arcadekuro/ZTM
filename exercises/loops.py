for item in 'I love to code':
    print(item)

# you can also use nesting to nest loops within each other

for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c', 'd']:
        print(item, x)

# Iterable (noun) - list, dictionary, tuple, set or string
# That you can iterate over - loop over something
# Iterated (action) - one by one to check each item in the collection.

user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}

# This will loop over the keys not values.
for item in user:
    print(item)

# To loop over the key/value pair:

for key, value in user.items():
    print(item)

# prints the values in the dictionary.
for item in user.values():
    print(item)

# prints the keys in the dictionary.
for item in user.keys():
    print(item)

