# move all zeros to the end
A = [5, 6, 0, 3, 6, 0, 9, 0, 7]
n = len(A)
j = 0
for i in range(n):
  if A[i]!=0:
    A[j],A[i]=A[i],A[j] # Partitioning the array
    j+=1
print(A)
