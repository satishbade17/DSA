def find_largest(n, arr):
    largest = arr[0]

    for i in range(1, n):
        if arr[i] > largest:
            largest = arr[i]

    return largest

# Input
arr = [10, 25, 8, 45, 30]

# Function Call
result = find_largest(len(arr), arr)

print("Largest element:", result)




#2nd_menthod
def find_largest(arr):
    largest = arr[0]

    for num in arr:
        if num > largest:
            largest = num

    return largest

arr = [10, 25, 8, 45, 30]

# Function Call
result = find_largest(arr)

print("Largest element:-", result)