'''Initialize variables of numerator and denominator
Take user input of two fraction
Find numerator using this condition (n1*d2) +(d1*n2 ) where n1,n2 are numerator and d1 and d2 are denominator
Find denominator using this condition (d1*d2) for lcm
Calculate GCD of a this new numerator and denominator
Display a two value of this condition x / gcd, y/gcd'''

def findGCD(n1, n2):
    gcd = 0
    for i in range(1, int(min(n1, n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcd = i
    return gcd
num1, den1 = map(int, list(input("Enter numerator and denominator of first number : ").split(" ")))
num2, den2 = map(int, list(input("Enter numerator and denominator of second number: ").split(" ")))
lcm = (den1 * den2) // findGCD(den1, den2)
sum = (num1 * lcm // den1) + (num2 * lcm // den2)
num3 = sum // findGCD(sum, lcm)
lcm = lcm // findGCD(sum, lcm)
print(num1, "/", den1, " + ", num2, "/", den2, " = ", num3, "/", lcm)


g1nume = int(input(‘Enter the numerator for 1st fraction :’))
g1deno = int(input(‘Enter the denominator for the 1st fraction :’))
g2nume = int(input(‘Enter the numerator for 2nd fraction :’))
g2deno = int(input(‘Enter the denominator for the 2nd fraction :’)) 
n = g1deno*g2deno
o = g2deno*g1nume
h = g1deno*g2nume
k = o + h 
print(k, ‘/’, n)
