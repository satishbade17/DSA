def subarraySum(nums,k):
        count = 0
        current_sum = 0
        sum_map = {0: 1}

        for num in nums:
            current_sum += num

            if current_sum - k in sum_map:
                count += sum_map[current_sum - k]

            if current_sum in sum_map:
                sum_map[current_sum] += 1
            else:
                sum_map[current_sum] = 1

        return count
nums = [1,1,1]
k = 2
print(subarraySum(nums,k))