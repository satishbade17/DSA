def Decimal_to_Octal(n):
    octal=0
    place=1
    
    while n>0:
        remainder=n%8
        octal=octal+remainder*place
        place=place*10
        n=n//8
    return octal
n = int(input("Enter decimal number: "))
print(Decimal_to_Octal(n))