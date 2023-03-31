import string
def print_rangoli(size):
    # your code goes here
    a=string.ascii_lowercase
    r=[]
    for i in range(size):
        s="-".join(a[i:size])
        r.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(r[:0:-1]+r))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
