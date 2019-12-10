arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        smallest_index = arr.index(min(arr[cur_index : ]))     


        # TO-DO: swap
        if cur_index != smallest_index:
            cur = arr.pop(cur_index)
            small = arr.pop(smallest_index -1)
            arr.insert(cur_index, small)
            arr.insert(smallest_index, cur)
        else:
            pass




    return arr
# print(selection_sort(arr1))

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    done = False
    while done == False:
        swaps = 0 
        for i in range(len(arr)):
            print(i)
            if i != len(arr) - 1:
                if arr[i] > arr[i + 1]:
                    #swap
                    cur = arr.pop(i)
                    small = arr.pop(i)
                    arr.insert(i, small)
                    arr.insert(i + 1, cur)
                    # add a swap
                    swaps += 1

        if swaps == 0:
            done = True


    return arr
print('bubble',bubble_sort(arr1))




# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr