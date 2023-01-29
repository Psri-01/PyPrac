class Apple:
    def __init__(self, color, flavor):   #init is a constructor which takes an argument called self, assigning values to the variables.
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
#By defining the special STR method, we're telling Python that we want it to display when the print function is called with an instance of our class.
jonagold = Apple("red", "sweet")
print(jonagold)
