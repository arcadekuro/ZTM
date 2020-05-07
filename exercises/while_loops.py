""" There are also while loops -
While a condiion is happening, do something.
This would print an infinite loop:

while 0 < 50:
    print(i)

Unless you use a break statement
to break out.
We can break out of the while loop as long as we can
turn a condition to false.

Else isn't that common next to while.
"""
i = 0
while i < 50:
    i += 10
    print(i)
else:  # special case for using a break statement - only excute w/o a break.
    print('done with all the work')

# When to use a while or for loop? Most useful way:


while True:
    input('say something: ')
    break  # after the input we will break out of the loop

while True:
    response = input('say something: ')
    if (response == 'bye'):
        break
