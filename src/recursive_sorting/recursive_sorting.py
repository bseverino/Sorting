# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    merged_arr = []

    # TO-DO
    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] < arrB[0]:
            merged_arr.append(arrA[0])
            arrA.pop(0)
        else:
            merged_arr.append(arrB[0])
            arrB.pop(0)

    for i in arrA:
        merged_arr.append(i)

    for i in arrB:
        merged_arr.append(i)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr) // 2
        left_arr = merge_sort(arr[:middle])
        right_arr = merge_sort(arr[middle:])

        return merge(left_arr, right_arr)
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    
    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
