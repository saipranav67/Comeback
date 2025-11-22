def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):

            # Swap if the current element is greater than the next one
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Example
nums = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", nums)
print("After sorting :", bubble_sort(nums))
