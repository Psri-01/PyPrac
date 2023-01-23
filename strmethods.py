print("mountains".upper())
print("MOUNTAINS".lower())
answer = 'YES'
if answer.lower()=="yes":
    print("User said yes")
#another method is strip, with lstrip and rstrip as variations- to get rid of whitespaces/tabs/nl to the left or right of the string
print("The number of times e occurs in this string is".count("e"))
print("Forest".endswith("rest"))
print("12345".isnumeric())
print(int("12345")+int("54321"))
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "dots"]))
print("Sometimes I feel like splitting people in half".split())

name="Manda"
number="1241590024"
print("Hello {}, your registration number is {}".format(name,number))
print("Your {} digit regno is {number},{name}.".format(len(number),name=name,number=number))

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name,grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price*1.09
print("Base price: ${:.2f}. With tax: ${:.2f}".format(price, with_tax)) 
# :.2f means we're going to format a float number and that there should be two digits after the decimal dot.

def to_celsius(x):
    return (x-32)*5/9
for x in range(0,101,10):
    print("{:>3} F | {:>6.2f} C".format(x,to_celsius(x)))
''' In the first expression we're saying we want the numbers to be aligned to the right for a total of three spaces. 
In the second expression we're saying we want the number to always have exactly two decimal places and we want to align it to the right at six spaces.'''
