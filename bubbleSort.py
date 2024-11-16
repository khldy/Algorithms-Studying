def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1) :
        swapped = False
        for j in range(n -i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            break
    return arr

numbers = [12, 6, 8 ,90, 54, 23 ,45 ,73, 5, 0]
print('Unsorted array: ', numbers)

sortedNumbers = bubble_sort(numbers)
print('Sorted array: ', sortedNumbers)