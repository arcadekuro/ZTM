
# Add code that allows us to access through index anyway a regular
# list allows us to.
# Super list should have a special dunder method

# Use inheritance to acquire the powers of list so that
# it becomes out parent class of Super list.


class SuperList(list):  # extend the functionality of list
    def __len__(self):
        return 1000


super_list1 = SuperList()

print(len(super_list1))
super_list1.append(5)
print(super_list1[0])
print(issubclass(SuperList, list))  # check if Superlist is a subclass of list
print(issubclass(list, object))

# Everything in python is an object that inherits from the base class object.
