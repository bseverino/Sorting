# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_smallest_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(i + 1, len(arr)):
            if arr[x] < arr[cur_smallest_index]:
                cur_smallest_index = x

        # TO-DO: swap
        arr[i], arr[cur_smallest_index] = arr[cur_smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False

        # compare adjacent elements
        # decrease range size by i with each pass
        # leave out final element as there is nothing after it to compare
        for x in range(len(arr) - i - 1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
                swapped = True

        if swapped == False:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
