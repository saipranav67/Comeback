def add(A, B):
    return [
        [A[i][j] + B[i][j] for j in range(len(A))]
        for i in range(len(A))
    ]


def subtract(A, B):
    return [
        [A[i][j] - B[i][j] for j in range(len(A))]
        for i in range(len(A))
    ]


def strassen(A, B):
    n = len(A)

    # Base case
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    # Split matrix A
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    # Split matrix B
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # Strassen’s 7 matrix multiplications
    M1 = strassen(add(A11, A22), add(B11, B22))
    M2 = strassen(add(A21, A22), B11)
    M3 = strassen(A11, subtract(B12, B22))
    M4 = strassen(A22, subtract(B21, B11))
    M5 = strassen(add(A11, A12), B22)
    M6 = strassen(subtract(A21, A11), add(B11, B12))
    M7 = strassen(subtract(A12, A22), add(B21, B22))

    # Combine result submatrices
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)

    # Combine final matrix
    result = []
    for i in range(mid):
        result.append(C11[i] + C12[i])
    for i in range(mid):
        result.append(C21[i] + C22[i])

    return result


# Driver code
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

C = strassen(A, B)

print("Result Matrix:")
for row in C:
    print(*row)
