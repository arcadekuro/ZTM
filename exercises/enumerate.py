
""" Have to give enumerate something it can iterate over.
It will give you an index counter and the item at that index.
e.g.
0 H
1 e
2 l
3 l
4 o """

for i, char in enumerate('Hellooo'):
    print(i, char)

# Creating a script that enumerates a list of numbers

for i, char in enumerate(list(range(101))):
    print(i, char)
    if char == 50:
        print(f'index of 50 is: {i}')
