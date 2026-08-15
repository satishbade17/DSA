def nextPermutation(nums):
    i = len(nums) - 2

    # Step 1: Find the first decreasing element
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: Find the element just larger than nums[i]
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the remaining part
    nums[i + 1:] = reversed(nums[i + 1:])

nums = [1, 2, 3]
nextPermutation(nums)
print(nums)