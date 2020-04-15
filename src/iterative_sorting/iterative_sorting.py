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

        """
        -Compare adjacent elements
        -Decrease range size by i with each pass
        -Leave out final element as there is nothing after it to compare
        """
        for x in range(len(arr) - i - 1):
            if arr[x] > arr[x+1]:
                arr[x], arr[x+1] = arr[x+1], arr[x]
                swapped = True

        if swapped == False:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    """
    -Create a count array to store the count of each item
    -Modify the count array so that each item adds the count of the previous element
    -Use the count array to determine the position of each element in a new array, decreasing the count by 1 each time
    """
    if len(arr) == 0:
        return arr

    count_arr = [0 for x in range(max(arr) + 1)]
    sorted_arr = [x for x in range(len(arr))]

    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:
            count_arr[i] += 1
    print(count_arr)
    
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]
    print(count_arr)

    for i in arr:
        sorted_arr[count_arr[i] - 1] = i
        count_arr[i] -= 1

    return sorted_arr