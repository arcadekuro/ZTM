
def outer():
    """
    Info: returns the outer variable.
    """
    x = "local"

    def inner():
        """
        Info: returns inner.
        """
        x = "nonlocal"
        print("inner: ", x)

    inner()  # modified the outerscope with nonloca
    print("outer: ", x)


outer()

# non local is a new keyword in python3
# advise against it because it makes the code less predictable

"""
Scope is what variables do I have access to?
# Python looks @
# 1. local variable
# 2. parent local?
# 3. Global
# 4. Inbuilt functions

"""
