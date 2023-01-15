def hint_username(username):
  if len(username) < 3:
    print("Invalid username. Must be atleast 3 chars long")
  elif len(username) > 15:
    print("Invalid username. Must be shorter than 15 chars")
  else:
    print("Valid username")
