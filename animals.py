animals = ["Lion","Zebra","Dolphin","Monkey"]
chars = 0
for animal in animals:
  chars += len(animals)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
