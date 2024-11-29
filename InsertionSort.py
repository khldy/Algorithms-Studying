def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] # Starting grom the second element
        j = i - 1 # The element on the left

        # Moving elements of arr[0..i -1] that are greater than the key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] # shifting
            j -= 1 # Stop the loop if j = -1

        arr[j + 1] = key

    return arr

# Usage

unsorted_list = [12, 11, 13, 5, 6]
sorted_list = insertion_sort(unsorted_list)
print('Sorted list: ', sorted_list)