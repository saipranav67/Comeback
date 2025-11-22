def counting_sort_digit(arr, n, exp):
    output = [0] * n
    count = [0] * 10

    # 1. Count occurrences of digits
    for i in range(n):
        digit = (arr[i] // exp) % 10
        count[digit] += 1

    # 2. Cumulative sum
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 3. Build output array (right → left for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    # 4. Copy output → arr
    for i in range(n):
        arr[i] = output[i]


# -----------------------------
# RADIX SORT – using LSD method
# -----------------------------
def radix_sort(arr):
    n = len(arr)

    # 1. Find maximum number
    max_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]

    # 2. Apply counting sort for each digit (1s, 10s, 100s...)
    exp = 1
    while max_val // exp > 0:
        counting_sort_digit(arr, n, exp)
        exp *= 10


# Example
nums = [170, 45, 75, 90, 802, 24, 2, 66]
print("Before sorting:", nums)
radix_sort(nums)
print("After sorting :", nums)
