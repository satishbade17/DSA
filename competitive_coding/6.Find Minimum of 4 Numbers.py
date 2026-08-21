def find_min(a, b, c, d):
    min_num = a

    if b < min_num:
        min_num = b

    if c < min_num:
        min_num = c

    if d < min_num:
        min_num = d

    return min_num

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

print("Minimum number is:", find_min(a, b, c, d))