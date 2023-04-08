def average(array):
    sum_array = sum(set(array))
    len_array = len(set(array))
    output = sum_array/len_array
    return output;
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    '''Ms. Gabriel Williams is a botany professor at District College. 
    One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:
avg = sum of total heights / total no. of distinct heights
'''
