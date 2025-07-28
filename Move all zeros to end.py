# Move all zeros to end
# https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1


def move_zeros_to_end(arr):
    n = len(arr)
    pos = 0  
    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    while pos < n:
        arr[pos] = 0
        pos += 1
    return arr
print(move_zeros_to_end([1, 2, 0, 4, 3, 0, 5, 0])) 
print(move_zeros_to_end([10, 20, 30]))   
print(move_zeros_to_end([0, 0]))         
