# Insert an element at end of array
# https://www.geeksforgeeks.org/problems/array-insert-at-end/1


def insert_at_end(arr, val):
    arr.append(val)
    return arr
arr1 = [1, 2, 3, 4, 5]
val1 = 90
print(insert_at_end(arr1, val1)) 
arr2 = [1, 2, 3]
val2 = 50
print(insert_at_end(arr2, val2)) 
