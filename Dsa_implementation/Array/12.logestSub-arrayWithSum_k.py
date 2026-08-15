def lenOfLongSubarr(arr, k):
    s = 0
    ans = 0
    mp = {}

    for i in range(len(arr)):
        s += arr[i]

        if s == k:
            ans = i + 1

        if s - k in mp:
            ans = max(ans, i - mp[s - k])

        if s not in mp:
            mp[s] = i

    return ans

print(lenOfLongSubarr([1,2,3,4], 6))