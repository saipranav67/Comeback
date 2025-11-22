def insertion_sort(bucket):
    n = len(bucket)
    for i in range(1, n):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def bucket_sort(arr):
    n = len(arr)

    # 1. Create n empty buckets
    buckets = []
    for i in range(n):
        buckets.append([])

    # 2. Insert elements into buckets
    for i in range(n):
        index = int(n * arr[i])  # bucket index
        buckets[index].append(arr[i])

    # 3. Sort individual buckets using insertion sort
    for i in range(n):
        insertion_sort(buckets[i])

    # 4. Concatenate buckets into original array
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1


# Example
nums = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print("Before sorting:", nums)
bucket_sort(nums)
print("After sorting :", nums)
