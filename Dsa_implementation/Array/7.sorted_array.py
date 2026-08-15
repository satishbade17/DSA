def SearchInSort(arr, n, k):
    p, q = 0, n - 1

    while p <= q:
        mid = (p + q) // 2

        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            p = mid + 1
        else:
            q = mid - 1

    return -1


arr = [1, 2, 5, 6, 8]  # Sorted
k = 6

print(SearchInSort(arr, len(arr), k))