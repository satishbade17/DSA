def count_substrings(s, k):
    n = len(s)
    count = 0

    for i in range(n):
        for j in range(i + k, n + 1):
            count += 1

    return count

s = "abs"
k = 2
print(count_substrings(s, k))