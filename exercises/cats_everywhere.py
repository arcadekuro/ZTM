# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

pep = Cat('pep', 12)
tom = Cat('Tom', 9)
aggie = Cat('Aggie', 3)


# 2 Create a function that finds the oldest cat
def oldest_cat(*args):
    return max(args)


# oldest = oldest_cat(pepper.age, tommy.age, aggie.age)

# 3 Print out: "The oldest cat is x years old.".
# x will be the oldest cat age by using

# print(f'The oldest cat is {oldest} years old.')
print(
    f'The oldest cat is {oldest_cat(pep.age, tom.age, aggie.age)} years old.')
