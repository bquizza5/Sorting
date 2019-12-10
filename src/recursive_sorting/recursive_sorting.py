# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    arrA = arrA
    arrB = arrB
    elements = len( arrA ) + len( arrB )
    merged_arr = []
    # TO-DO
    while len( arrA ) + len( arrB ) > 0:
        if len(arrA) == 0 or len(arrB) == 0:
            merged_arr = merged_arr + arrA + arrB
            return merged_arr
        else:
            if arrA[0] <= arrB[0]:
                num1 = arrA.pop(0)
                merged_arr.append(num1)
            else:
                num1 = arrB.pop(0)
                merged_arr.append(num1)
    return merged_arr
# print(merge([2,4,5],[1,3,6]))


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    half = int(len(arr)/2)

    if len(arr) == 1:
        return arr
    elif len(arr) == 0:
        return arr
    else:
        return merge(merge_sort(arr[:half]), merge_sort(arr[half:]))
    # return arr

print(merge_sort([4,4,3,6,1,2,7,9,10,15,16,17,18,12,13,14,14]))
print(merge_sort([]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
