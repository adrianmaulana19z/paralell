def matrix_multiply(A, B):
    N = len(A)
    C = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    return C

A = [[4, 6], [9, 11]]
B = [[3, 5], [4, 8]]

print(matrix_multiply(A, B))