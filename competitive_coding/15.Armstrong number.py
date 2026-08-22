def Armstrong_number(n):
    temp=n
    digit=0
    
    while temp>0:
        digit=digit +1
        temp=temp //10
    
    temp=n
    sum=0
    
    #calulate armstrong sum
    while temp>0:
        digits=temp%10
        sum=sum + digits ** digit
        temp=temp//10
        
    if sum==n:
        return"Armstrong Number"
    else:
        return "Not an armstrong Number"
        
n = int(input("Enter a number: "))
print(Armstrong_number(n))
        
        