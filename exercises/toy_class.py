class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.my_dict = {
            'name': 'yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 5

    def __call__(self):  # this is how we call functions under the hood.
        return print('yess?')

    def __getitem__(self, i):
        return self.my_dict[i]


action_figure = Toy('red', 0)
print(action_figure.__str__())  # prints the location of toy in memory

# this is the same as:
print(str('action_figure'))
print(len(action_figure))
# del action_figure # delete can cause bugs we want to avoid.
print(action_figure())

print(action_figure['name'])  # using bracket notation
