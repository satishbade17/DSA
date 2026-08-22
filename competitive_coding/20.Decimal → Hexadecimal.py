def Decimal_to_Hexadecimal(n):
    hexadecimal=""
    digits="0123456789ABCDEF"
    
    while n>0:
        remainder=n%16
        hexadecimal=digits[remainder]+hexadecimal
        n=n//16
    
    return hexadecimal
n = int(input("Enter decimal number: "))
print(Decimal_to_Hexadecimal(n))

        
    