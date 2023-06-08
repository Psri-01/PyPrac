'''Steps in detail:

Initialize a counter variable to keep the track of the frequency of the digit.
Make the number positive if it is not already.
Extract the unit digit from the number and compare it with the digit. If they are equal, then increment the counter.
Divide the number by 10 and update it.
Keep repeating the process until the number is reduced to Zero.'''

# Function returns
def digit_frequency_calculator(num, digit):
    counter = 0 # Counter to keep the track of frequency of digit in the num 
    while(num):
        unit_digit = num%10        # Get the unit digit 
        if unit_digit == digit:
            counter = counter + 1
        num = num // 10 # same as num = int(num/10)
    return counter


# Get the absolute value of the integer. 
# Second parameter is the number whose frequency we want to calculate
digit_frequency_calculator(abs(-1321818181), 8)

#Output 
3
