#GCD (Greatest Common Divisor) or HCF (Highest Common Factor)

#1.Using Built-in Function
import math
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("GCD/HCF",math.gcd(num1,num2))


#2.method
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
        return a
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("GCD/HCF =", gcd(num1, num2))