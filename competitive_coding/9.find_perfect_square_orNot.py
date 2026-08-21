#Method 1: Using math.sqrt()
import math
n=int(input("Enter a number:"))
root=int(math.sqrt(n))
if root*root==n:
    print("perfect square")
else:
    print("Not a perfect square")
    
    
#Method 2: Without using sqrt()
n=int(input("Enter a number:"))
i=1
while i*i<=n:
    if i*i==n:
        print("perfect square")
        
        break
    i+=1
    
else:
    print("Not a perfect square")