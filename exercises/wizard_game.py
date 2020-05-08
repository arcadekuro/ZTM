"""
learning about classes.
brief =  game company wants to create
a wizard game
how to think about it in OOP.

When creating a class it should be signular:
IT IS A blueprint & we will create characterS from it.

"""
# when creating class it should be a singular.


class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name  # attributes/properties
        self.age = age

    def run(self):
        print('run')
        return 'done'


# instantiate the class
def create_character():
    player = input('what is your name?\n')
    age = input('what is your age?\n')
    specs = player + age
    player = PlayerCharacter(player, specs)
    # print(player) - prints the object type and location.
    return player


player1 = create_character()
help(player1)
