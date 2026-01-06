def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        # start from the 2nd element
        unsorted_num = arr[i]

        # consider 1st element to be sorted
        j = i - 1

        # shift element to right until correct position found
        while j >= 0 and arr[j] > unsorted_num:
            arr[j+1] = arr[j]
            j -= 1

        #insert the unsorted num at correct position
        arr[j+1] = unsorted_num

    return arr

arr = [12, 11, 13, 5 , 6]
sorted_arr = insertion_sort(arr)
print('sorted_arr ' , sorted_arr)
