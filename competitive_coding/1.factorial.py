def factorial(n):
    if n == 0 or n == 1:
        return 1

    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

n= int(input("Enter a number: "))
print("Factorial:", factorial(n))

#Recursive Version
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print("Factorial:", factorial(n))