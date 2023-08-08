def chocolateDistribution(arr,n,m):
    arr.sort()
    if(m>n):
        return -1
    start=0
    end=m-1
    min_diff=arr[end]-arr[start]
    while end<n:
        diff=arr[end]-arr[start]
        if diff<min_diff:
            min_diff=diff
        start+=1
        end+=1
    return min_diff
print(chocolateDistribution([10,29,5,20,37,56,12],7,5))
