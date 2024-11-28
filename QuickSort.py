def quick_sort(array, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(array, low, high)

        # Recursively sort elements before and after the partition
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)


def partition(array, low, high):
    # Choose the pivot (last element in this case)
    pivot = array[high]
    i = low - 1  # Index for smaller elements

    for j in range(low, high):
        # If the current element is smaller than or equal to the pivot
        if array[j] <= pivot:
            i += 1
            # Swap elements
            array[i], array[j] = array[j], array[i]

    # Place the pivot in the correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1


# Example Usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)
