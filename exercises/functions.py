def say_hello(name, emoji):
    print(f'hello {name}, {emoji}')


# call the function below
say_hello('Arcade', '😘')

# beyond repetition we can make functions dynamic
# can give parameters - when defining function
# arguments when calling/invoking the function.

# Keyword arguments - not worry about positional

# However, bad practice as it's more complicated.
say_hello(emoji='😘', name='love')

# default parameters - alows a default to be printed.
# In case you forget to pass arguments when calling the function


def hi_darth(name='Darth Vader', emoji='😈'):
    print(f'{name} you can\'t be my father!\n'
          f'yes I am luke {emoji}')


hi_darth()
