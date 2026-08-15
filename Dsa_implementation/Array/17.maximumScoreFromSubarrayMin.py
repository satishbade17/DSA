def pairwithmaxsum(arr):
    max_sum=0
    for i in range(len(arr)-1):
        current_sum=arr[i]+arr[i+1]
        max_sum=max(max_sum,current_sum)
    return max_sum
arr=[4,3,1,5,6]
print(pairwithmaxsum(arr))