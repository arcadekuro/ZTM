""" A GUI or graphical user interface

print(picture[1])

# my 1st attempt
for item in picture:
    for i in picture[1]:
        if i == 0:
            print(' ')
        elif i == 1:
            print('*')
"""

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# 1 Iterate over picture
# if 0 -> print ' '
# if 1 -> print *

fill = '*'
empty = ''

for row in picture:
    for pixel in row:
        if pixel == 1:  # truthy value so don't need one
            print(fill, end='')  # end rm the default of printing new line
        else:
            print(empty, end='')
    print(' ')  # need a new line after every row
