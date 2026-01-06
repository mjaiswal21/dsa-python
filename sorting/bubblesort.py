def bubble_sort(arr):

    n = len(arr)

    for i in range(n-1):
        swapped = False

        for j in range(n - 1 - i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

arr =[5, 3, 8, 4, 2]
sorted_arr = bubble_sort(arr)
print('sorted arr ', sorted_arr)

