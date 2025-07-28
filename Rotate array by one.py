# Rotate array by one
# https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1


def rotate_by_one(arr):
    if len(arr) == 0:
        return arr 
    last = arr[-1]  
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    return arr
print(rotate_by_one([1, 2, 3, 4, 5]))            
print(rotate_by_one([9, 8, 7, 6, 4, 2, 1, 3]))   
