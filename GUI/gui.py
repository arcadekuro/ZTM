picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

print(picture[1])

# my attempt 
for image in picture:
    for pixel in picture[1]:
        if i == 0:
            print(' ')
        elif i == 1:
            print('*')

# 1 Iterate over picture
    # if 0 -> print ' '
    # if 1 -> print *