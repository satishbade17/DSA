def rearrangeArray(nums):
        positives=[]
        negatives=[]

        for num in nums:
            if num >0:
                positives.append(num)
            else:
                negatives.append(num)
        result=[]

        for i in range (len(positives)):
            result.append(positives[i])
            result.append(negatives[i])
        return result
nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))     