import sys
from random import randint
# generate a number between 1 and 10.
answer = randint(int(sys.argv[1]), int(sys.argv[2]))

# input from user

# check if number is between 1 and 10
while True:
    try:
        guess = int(
            input(f'guess a number {sys.argv[1]} through {sys.argv[2]}!:\n'))
        if int(sys.argv[1]) < guess < int(sys.argv[2] + 1):
            if guess == answer:
                print('you\'re a Genius!')
                break
        else:
            print(f'hey bozo! I said between {sys.argv[1]}~{sys.argv[2]}!')
    except ValueError:
        print('please enter a number!')
        continue
# check number is the same
