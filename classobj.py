class Flower:
  color = 'unknown'

rose = Flower()
rose.color = "red"

violet = Flower()
violet.color = "blue"

this_pun_is_for_you = Flower()

print("Roses are {},".format(rose.color))
print("violets are {},".format(violet.color))
print(this_pun_is_for_you) 

class Piglet:
  years = 0
  def pig_years(self):
    return self.years*18
piggy = Piglet()
print(piggy.pig_years())
piggy.years = 2
print(piggy.pig_years())

#similar to piggy example
class Dog:
  years = 0
  def dog_years(self):
    return self.years*7
fido = Dog()
fido.years = 3
print(fido.dog_years())

class Apple:
  color = ""
  flavor = ""
jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color)
print(jonagold.flavor)
print(jonagold.color.upper())
#similarly
golden = Apple()
golden.color = "gold"
golden.flavor = "soft"
print(golden.color)
print(golden.flavor)

class Apple:
    def __init__(self, color, flavor):   #init is a constructor which takes an argument called self, assigning values to the variables.
        self.color = color
        self.flavor = flavor
jonagold = Apple("gold", "soft")
print(jonagold.color)
print(jonagold.flavor)

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return "hi, my name is {}".format(self.name)

# Create a new instance with a name of your choice
some_person = Person("Grisha")
# Call the greeting method
print(some_person.greeting())
