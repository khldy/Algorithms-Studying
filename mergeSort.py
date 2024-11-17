def merge_sort(arr):
    if len(arr) > 1:
        #finding ther middle of the array
        mid = len(arr) // 2

        #Dividing the elements into two halves
        left_half = arr[:mid] #all elements till the mid
        right_half = arr[mid:] #all the elements after the mid

        #sorting both halves recursively
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        #Merging sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        #Checking if there are elements left in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        #checking if any elements left in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


#Usage

array = [12, 50, 5, 9, 4, 0 ,80, 123]
print('Original array: ', array)

merge_sort(array)

print('Sorted array: ', array)

