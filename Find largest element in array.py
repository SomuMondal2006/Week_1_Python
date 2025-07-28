# Find largest element in array
# https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1


def find_largest(arr):
    largest = arr[0]
    for num in arr[1:]:
        if num > largest:
            largest = num
    return largest
print(find_largest([1, 8, 7, 56, 90]))  
print(find_largest([5, 5, 5, 5]))       
print(find_largest([10]))               
