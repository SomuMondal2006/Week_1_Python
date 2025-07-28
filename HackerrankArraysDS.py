# Hackerrank: Arrays - DS
# https://www.hackerrank.com/challenges/arrays-ds/problem


def reverseArray(A):
    return A[::-1]  
def main():
    N = int(input("Enter the number of elements: "))
    A = list(map(int, input("Enter the elements separated by space: ").split()))
    if len(A) != N:
        print("Error: Number of elements doesn't match the given size.")
        return
    result = reverseArray(A)
    print("Reversed array:", " ".join(map(str, result)))
if __name__ == "__main__":
    main()
