
def mergesort(arr):
    if(len(arr)<=1):
        return

    mid = len(arr)//2
    left_arr = arr[ : mid]
    right_arr = arr[mid : ]

    mergesort(left_arr)
    mergesort(right_arr)

    #Merge
    merge_two_sorted(left_arr, right_arr, arr)



def merge_two_sorted(left_arr, right_arr, arr):

    i = 0
    j = 0
    k = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i+=1

        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i+=1
        k+=1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j+=1
        k+=1



arr = [2, 6, 4, 23, 45, 8, 1, 59, 3]
mergesort(arr)
print(arr)