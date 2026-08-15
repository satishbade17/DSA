def check(num):
    n=len(num)
    if n==1:
        return True
    count=0
    for i in range(n):
        if num[i]>num[(i+1)%n]:
            count+=1
    return count<=1
num=[3,4,5,1,2]
result=check(num)
print("array is sorted and rotated",result)