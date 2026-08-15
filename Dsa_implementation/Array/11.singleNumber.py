def singleNumber(nums):
    result=0
    for num in nums:
        result^=num
    return result
nums=[2,2,3,4]
nums = [2, 2, 1]
print(singleNumber(nums))
    