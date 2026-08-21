def find_second_largest(a, b, c):
    if a >= b and a >= c:
        if b >= c:
            return b
        else:
            return c

    elif b >= a and b >= c:
        if a >= c:
            return a
        else:
            return c

    else:  # c is largest
        if a >= b:
            return a
        else:
            return b
print(find_second_largest(10, 20, 30))  # 20
print(find_second_largest(50, 20, 30))  # 30
print(find_second_largest(10, 40, 30))  # 30



arr = [10, 20, 30, 40, 50]

largest = second_largest =-1

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest:", second_largest)