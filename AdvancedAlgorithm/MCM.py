# Python code to implement the
# matrix chain multiplication using tabulation

def matrixMultiplication(arr):
    n = len(arr)

    # Create a 2D DP array to store min
    # multiplication costs
    dp = [[0] * n for _ in range(n)]

    # Fill the DP array
    # length is the chain length
    for length in range(2, n):
        for i in range(n - length):
            j = i + length
            dp[i][j] = float('inf')

            for k in range(i + 1, j):
                cost = dp[i][k] + dp[k][j] + arr[i] * arr[k] * arr[j]
                dp[i][j] = min(dp[i][j], cost)

    # Minimum cost is in dp[0][n-1]
    return dp[0][n - 1]


arr = []
n=int(input("Enter number of matrices: "))
print("Enter dimension: ")
for i in range(0,n+1):
    d=int(input())
    arr.append(d)
print("Min cost",matrixMultiplication(arr))