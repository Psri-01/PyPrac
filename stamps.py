n = int(input())
stamps = set()
while n>0:
    stamps.add(input())
    n-=1
print(len(stamps))

'''Task
Apply your knowledge of the .add() operation to help your friend.
She has a huge collection of country stamps. She decided to count the total number 
of distinct country stamps in her collection. She asked for your help. 
You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.'''
