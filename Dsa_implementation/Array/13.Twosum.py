def twosum(nums, target):
    s = {}

    for index, num in enumerate(nums):
        complement = target - num

        if complement in s:
            return [s[complement], index]

        s[num] = index

    return []

nums = [2, 7, 11, 15]
target = 9

print(twosum(nums, target))