import math
def nearest_power_of_two(n):
    power = math.floor(math.log2(n))
    return pow(2, power)
t = int(input())
while t > 0:
    n = int(input())
    k = 0
    winner = 1  # 1 - Richard, 0 - Louise
    while n != 1:
        if n & (n - 1) == 0:
            n //= 2
        else:
            k = nearest_power_of_two(n)
            n -= k
        if winner:
            winner = 0
        else:
            winner = 1
    if winner:
        print("Richard")
    else:
        print("Louise")
    t -= 1
