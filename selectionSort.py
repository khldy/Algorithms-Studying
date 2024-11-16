def selection_sort(arr):
    for i in range(len(arr)):  # Iterating through the full array, starting from the first index
        min_index = i  # Assuming the current index holds the smallest value
        for j in range(i + 1, len(arr)):  # Iterating starting from the next index to compare all remaining elements
            if arr[j] < arr[min_index]:  # Comparing the current element with the current minimum
                min_index = j  # If a smaller element is found, update min_index

        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the current element with the found minimum element
    return arr  # Return the sorted array

numbers = [64, 25, 12, 22, 11]
print('Unsorted array: ', numbers)  # Print the unsorted array

sortedNumbers = selection_sort(numbers)  # Call the selectionSort function and store the result in sortedNumbers
print('Sorted Array: ', sortedNumbers)  # Print the sorted array
