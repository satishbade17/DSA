arr=[1,2,5,2,3,2,4]
target=2
first=-1
last=-1
for i in range(len(arr)):
    if arr[i]==target:
        if first==-1:
            first=i
        last=i

print("First occurrence:-",first)
print("last occurrence:-",last)


        