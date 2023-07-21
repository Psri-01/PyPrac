n=28
sum=0
for i in range(1,n):
  if n%i==0:
    sum=sum+i
if sum==n:
  print('Perfect num')
else:
  print('Imperfect num')

num = 28
sum = 0
i = 1
while i < num:
    if num % i == 0:
        sum += i
    i += 1
if sum == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")

num = 28
sum = 0
for i in range(1, num//2 + 1):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("The number is a Perfect number")
else:
    print("The number is not a Perfect number")
