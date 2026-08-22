#Method 1: Using a string (Simplest)

num=int(input("entre a Number:"))
for digit in str(num):
    print(digit)
    
#Method 2: Without converting to a string (Using recursion)

def print_digits(n):
    if n<10:
        print(n)
    else:
        print_digits(n//10)
        print(n%10)

num=int(input('Entre a number:'))
print_digits(num)