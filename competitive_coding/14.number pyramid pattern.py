def number_pyramid_pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end="*")
        print()
        
    
    for i in range(n-1,0,-1):
        for j in range(i):
            print(i,end="*")
        print()   
n=int(input("entre the numbrs:-"))
print(number_pyramid_pattern(n))   




n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
        if j < i - 1:
            print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print(i, end="")
        if j < i - 1:
            print("*", end="")
    print()      