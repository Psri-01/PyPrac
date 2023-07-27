def thrive(n):
 if n % 15 == 0:
   print("thrive", end = “ ”)
 elif n % 3 != 0 and n % 5 != 0:
   print("neither", end = “ ”)
 elif n % 3 == 0:
   print("three", end = “ ”)
 elif n % 5 == 0:
   print("five", end = “ ”)
thrive(35)
thrive(56)
thrive(15)
thrive(39)
#five neither thrive three

a = [1, 2]
print(a * 3)
#[1,2,1,2,1,2]

numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
even = lambda a: a % 2 == 0
even_numbers = filter(even, sorted_numbers)
print(type(even_numbers))
#filter

numbers = (4, 7, 19, 2, 89, 45, 72, 22)
sorted_numbers = sorted(numbers)
odd_numbers = [x for x in sorted_numbers if x % 2 != 0]
print(odd_numbers)
#[7,19,45,89]

dict1 = {'first' : 'sunday', 'second' : 'monday'}
dict2 = {1: 3, 2: 4}
dict1.update(dict2)
print(dict1)
#{'first':'sunday','second':'monday',1:3,2:4}

s = {1, 2, 3, 3, 2, 4, 5, 5}
print(s)
#sets only store unique elems so {1,2,3,4,5}

a = {'Hello':'World', 'First': 1}
b = {val: k for k , val in a.items()}
print(b)
#This is an example of dict comprehension in Python, reversing the key-value pairs from the 1st dictionary into the 2nd.
#{'World':'Hello',1:'First'}

'''strptime refers to parsing time which is used to read time in specific format. 
Whereas strftime refers to formatting time, which we use to change the format of time to some new format.'''

word = "Python Programming"
n = len(word)
word1 = word.upper()
word2 = word.lower()
converted_word = ""
for i in range(n):
 if i % 2 == 0:
   converted_word += word2[i]
 else:
   converted_word += word1[i]
print(converted_word)
#pYtHoN PrOgRaMmInG

a = "4, 5"
nums = a.split(',')
x, y = nums
int_prod = int(x) * int(y)
print(int_prod)
#20

square = lambda x: x ** 2
a = []
for i in range(5):
   a.append(square(i))   
print(a)
#[0,1,4,9,16]

def tester(*argv):
   for arg in argv:
       print(arg, end = ' ')
tester('Sunday', 'Monday', 'Tuesday', 'Wednesday')
# Sunday Monday Tuesday Wednesday
# We pass a variable number of arguments into the function using *args, and then print their value.
# *args are stored in Python as a tuple.

def tester(**kwargs):
   for key, value in kwargs.items():
       print(key, value, end = " ")
tester(Sunday = 1, Monday = 2, Tuesday = 3, Wednesday = 4)
# Sunday 1 Monday 2 Tuesday 3 Wednesday 4
# We can pass multiple key-word arguments to a function using kwargs. Here, we print the arguments passed to the function in this code snippet.
# *kwargs are stored in Python as a dictionary.

from math import *
a = 2.19
b = 3.999999
c = -3.30
print(int(a), floor(b), ceil(c), fabs(c))
# 2 3 -3 3.3

set1 = {1, 3, 5}
set2 = {2, 4, 6}
print(len(set1 + set2))
# Error

s1 = {1, 2, 3, 4, 5}
s2 = {2, 4, 6}
print(s1 ^ s2)
# The ^ operator in sets will return a set containing common of elements of its operand sets. so {1.3.5.6}

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
c = [x for x in a if x not in b]
print(c)
# [1,2]

# \n, \t and \\ are valid escape sequences in Python.
# Assertions can be disabled in Python passing -O when running Python.
a = [[], "abc", [0], 1, 0]
print(list(filter(bool, a)))
# ['abc',[0],1]
