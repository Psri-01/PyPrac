# A Harshad number is a number that is divisible by the sum of its digits.
def is_harshad_number(num):
    digits = str(num)
    digit_sum = sum(int(digit)for digit in digits)
    return num % digit_sum == 0
print(is_harshad_number(18))  # True, 1 + 8 = 9, 18 is divisible by 9
print(is_harshad_number(19))  # False, 1 + 9 = 10, 19 is not divisible by 10
print(is_harshad_number(202)) # F
print(is_harshad_number(153)) # True, 1 + 5 + 3 = 9, 153 is divisible by 9
print(is_harshad_number(100)) # T
print(is_harshad_number(408)) # T
