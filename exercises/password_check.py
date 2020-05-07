username = input('Please enter your username \n')
password = input('please enter your password \n')
hidden_password = '*' * len(password)

print(f"{username}, your  password {hidden_password}"
      "is {len(password)} letters long")
