username = get_username()
while not valid_username(username):
  print("Invalid username")
  username = get_username()
