""" my_file = open('test.txt')

# print(my_file.readlines())
my_file.seek(0)
my_file.close()
"""

# This way there is no need to close the file
with open('app/text2.txt', mode='a') as my_file:
    text = my_file.write('\n bruh!')
    print(text)

try:
    with open('hay.txt', mode='w') as file_new:
        file_new.write('haaaay gurlfirend')
except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err:
    print('IO erro')
    raise err
