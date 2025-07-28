# Find second largest element
# https://www.geeksforgeeks.org/problems/second-largest3735/1


def second_largest(arr):
    first = second = -1
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second
print(second_largest([12, 35, 1, 10, 34, 1])) 
print(second_largest([10, 5, 10]))            
print(second_largest([10, 10, 10]))           
