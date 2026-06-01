from multiprocessing import Pool
from heapq import merge


# Sort each chunk
def sort_part(part):
    return sorted(part)


# Parallel sorting
def parallel_sort(arr):

    mid = len(arr) // 2

    parts = [
        arr[:mid],
        arr[mid:]
    ]

    with Pool(processes=2) as p:
        sorted_parts = p.map(
            sort_part,
            parts
        )

    return list(
        merge(
            *sorted_parts
        )
    )


# Main execution
if __name__ == "__main__":

    arr = [
        170,
        45,
        75,
        90,
        802,
        24,
        2,
        66
    ]

    print("Array before sorting:")
    print(arr)

    result = parallel_sort(arr)

    print("\nArray after sorting:")
    print(result)