# Check if array is sorted
# https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
print(is_sorted([10, 20, 30, 40, 50]))         
print(is_sorted([90, 80, 100, 70, 40, 30]))    
