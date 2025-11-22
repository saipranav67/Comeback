def counting_sort(arr):
    n = len(arr)

    # 1. Find the maximum element
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num

    # 2. Create count array
    count = [0] * (max_val + 1)

    # 3. Store the count of each element
    for num in arr:
        count[num] += 1

    # 4. Modify count array to store cumulative sum
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 5. Create output array
    output = [0] * n

    # 6. Build the output array (stable sorting)
    for i in range(n - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # 7. Copy output back to arr
    for i in range(n):
        arr[i] = output[i]


# Example
nums = [4, 2, 2, 8, 3, 3, 1]
print("Before sorting:", nums)
counting_sort(nums)
print("After sorting :", nums)
