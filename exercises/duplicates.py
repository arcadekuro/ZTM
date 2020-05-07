
# remove duplicates from some_list
some_list = ['a', 'b', 'b', 'c', 'd', 'm', 'n', 'n']


duplicates = []

for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
