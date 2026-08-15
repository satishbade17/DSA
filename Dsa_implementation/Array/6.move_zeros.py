def moveZeros(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j],nums[i]=nums[i],nums[j]
            j+=1
    return nums
nums=[1,2,0,3,0,4]

print(moveZeros(nums))