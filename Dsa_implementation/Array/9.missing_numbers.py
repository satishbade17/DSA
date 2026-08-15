def missingNumber(nums):
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=sum(nums)
        return expected_sum-actual_sum
    
nums=[0,2,3]
print(missingNumber(nums))
