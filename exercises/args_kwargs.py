# *args *kwargs


def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
        print(kwargs)
    return sum(args) + total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# rule: params, *args, default parameters, **kwargs e.g:


def another_fun(name, *args, i='hi', **kwargs):  # as a rule this is bad code.
    pass
