def guess_age(n):
    birth_year = int(input('what year were you born?\n'))
    current_year = 2020
    age = current_year - birth_year
    print(f"You are {age} years old")

# guess_age(1994)


# another solution

birth_year = int(input('What year were you born?'))
age = 2019 - birth_year
print(f'Your age is: {age}')
