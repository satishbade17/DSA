def leaders(n, arr):
    leaders = []
    max_right = arr[-1]
    leaders.append(max_right)

    for i in range(n - 2, -1, -1):
        if arr[i] >= max_right:
            leaders.append(arr[i])
            max_right = arr[i]

    leaders.reverse()
    return leaders

arr = [17, 17, 4, 3, 5, 2]
print(leaders(len(arr), arr))