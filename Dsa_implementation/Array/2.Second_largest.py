def second_largest_element(arr):
    largest = second_largest = -1

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


arr = [10, 25, 8, 45, 30]

result = second_largest_element(arr)

print("Second Largest element:", result)