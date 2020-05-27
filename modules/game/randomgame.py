
import random
# generate a number between 1 and 10.


# input from user
# guess = int(input(f'guess a number 1 through 10 \n'))


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you\'re a Genius!')
            return True
    else:
        print(f'hey bozo! I said between 1 ~ 10!')
        return False


# check if number is between 1 and 10
if __name__ == '__main__':
    answer = random.randint(1, 10)
    while True:
        try:
            guess = int(input(f'guess a number 1 through 10 \n'))
            if run_guess(guess, answer):
                break
        except ValueError:
            print('please enter a number!')
            continue
