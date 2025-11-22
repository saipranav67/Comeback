def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
    return arr

# Example
nums = [12, 11, 13, 5, 6]
print("Before sorting:", nums)
print("After sorting:", insertion_sort(nums))
