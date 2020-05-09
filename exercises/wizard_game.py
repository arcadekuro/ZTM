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


class User():
    def sign_in(self):
        return 'logged in'


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left - {self.num_arrows}')


wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 100)
# inherited the functionality.
print(wizard1.sign_in())

wizard1.attack()
