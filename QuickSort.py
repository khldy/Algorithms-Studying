def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # Swapping

    # Place the pivot on its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1 #the pivot

def quick_sort(arr, low, high):
    if low < high:
        # Partitioning the array and getting rhe pivot
        pivot_index = partition(arr, low, high)

        # Recursively sort elements before and after the partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)


#Usage
array = [4, 2, 8, 60, 13, 1, 55]
arr = [10, 7, 8, 9, 1, 5]
quick_sort(array, 0, len(array) - 1)
print("Sorted array: ", array )
