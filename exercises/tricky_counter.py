""" Counter  for the items in our list."""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

counter = 0
for item in my_list:
    counter = counter + item

# print(counter)

# You can iterate over a range.
# you can also use an underscore instead of a variable.

for _ in range(11):
    print(_)

# Range also comes with the step over parameter.
# can also do descending using negative stepover
for _ in range(10, 0, -2):
    print(_)

# Quick way to create a range that also has lists
for n in range(2):
    print(list(range(10)))
