#right
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def right_rotate(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, n - 1) # Reverse whole array
    reverse(arr, 0, k - 1) # Reverse first k elements
    reverse(arr, k, n - 1) # Reverse remaining elements

    return arr

arr = [1, 2, 3, 4, 5]
k = 2

print(right_rotate(arr, k))


#Left
def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_rotate(arr, k):
    n = len(arr)
    k = k % n

    reverse(arr, 0, k - 1)    # Reverse first k elements
    reverse(arr, k, n - 1)    # Reverse remaining elements
    reverse(arr, 0, n - 1)    # Reverse whole array

    return arr

arr = [1, 2, 3, 4, 5]
k = 2

print(left_rotate(arr, k))