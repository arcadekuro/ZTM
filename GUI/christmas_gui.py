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


def show_tree():
    for image in picture:
        for pixel in image:
            if (pixel):  # truthy value so don't need  one
                print('*', end='')  # end rms the   default of print new line
            else:
                print('', end='')
        print('')  # need a new line after every row


show_tree()
