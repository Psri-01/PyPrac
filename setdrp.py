'''You have a non-empty set s, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
The first line contains integer N, the number of elements in the set.
The second line contains N space-separated elements of set. All of the elements are non-negative integers, less than or equal to 9.
The third line contains integer, the number of commands.
The next N  lines contains either pop, remove and/or discard commands followed by their associated value.'''
n = int(input())
s = set(map(int, input().split()))
N = int(input()) #num of commands
for i in range(N):
    cmd = list(map(str,input().split()))
    if cmd[0] == "pop":
        s.pop()
    elif cmd[0] == "remove":
        try:
            s.remove(int(cmd[1]))
        except:
            continue
    elif cmd[0] =="discard":
        try:
            s.discard(int(cmd[1]))
        except:
            continue
print(sum(s))
