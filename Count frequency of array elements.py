# Count frequency of array elements
# https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/1


def frequencyCount(arr):
    n = len(arr)
    freq = [0] * n  
    for num in arr:
        if 1 <= num <= n:
            freq[num - 1] += 1  
    return freq
print(frequencyCount([2, 3, 2, 3, 5]))   
print(frequencyCount([3, 3, 3, 3]))      
print(frequencyCount([1]))               
