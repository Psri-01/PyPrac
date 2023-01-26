cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for beast,arms in cool_beasts.items():
    print("{} have {}".format(beast, arms))
    
for ext in file_counts:
  print(extension)

for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext)
        
file_counts.keys()
file_counts.values()
        
for value in file_counts.values():
   print(value)

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
#output:
{'shirt': ['red', 'blue', 'white'], 'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
