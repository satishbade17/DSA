def setZeroes(matrix):
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    zero_rows = set()
    zero_cols = set()

    # Step 1: Find rows and columns containing 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Step 2: Set the corresponding rows and columns to 0
    for i in range(m):
        for j in range(n):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
    
    return matrix


# Example
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

print(setZeroes(matrix))