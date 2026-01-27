def maxSubArray(arr):
    max_sum = arr_sum = arr[0]
    for v in arr[1:]:
        arr_sum = max(v, arr_sum + v)
        max_sum = max(max_sum, arr_sum)
    return max_sum

arr = list(map(int, input("enter elements: ").split()))
print("Maximum Subarray Sum:", maxSubArray(arr))
