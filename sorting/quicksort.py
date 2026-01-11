def partition(arr, left, right):
    pivot_index = left
    pivot = arr[left]

    while left < right:

        while arr[left] <= pivot and left < right:
            left+=1

        while arr[right] > pivot:
            right-=1
        #swap left and right
        if left < right:
            arr[left] , arr[right] = arr[right] , arr[left]

    #swap left with pivot
    arr[pivot_index] , arr[right] = arr[right], arr[pivot_index]

    return right




def quicksort(arr, left , right):

    if left < right:
        pi = partition(arr,left, right)
        quicksort(arr, left, pi-1)
        quicksort(arr, pi+1 , right)


arr=[3,9,4,7,59,2,45,17,90,21]
quicksort(arr, 0 , len(arr) -1)
print(arr)
