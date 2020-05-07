
"""
args is a form of tuple.
It allows to pass any number of arguments well calling a function.
kwargs allows variable assignment of the arguments.
"""


def func1(*args, **kwargs):
    """function for printing a range in the parameter """
    for i in args:
        print(i + **kwargs)


func1(10=1, 30=2, 40, 50, 'this is super cool')
