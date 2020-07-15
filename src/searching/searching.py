# TO-DO: Implement a recursive implementation of binary search
import math

def binary_search(arr, target, start, end):
    if len(arr) <= 0:
        return -1

    mid = int(math.floor((end + start)/2))

    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    elif arr[mid] == target:
        return mid



# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    upper = len(arr) - 1
    lower = 0

    if arr[upper] > arr[lower]:
        while lower <= upper:
            mid = int(math.floor((upper + lower)/2))
            
            if target < arr[mid]:
                upper = mid - 1
            elif target > arr[mid]:
                lower = mid + 1
            elif target == arr[mid]:
                return mid
    else:
        while lower <= upper:
            mid = int(math.floor((upper + lower)/2))
            
            if target > arr[mid]:
                upper = mid - 1
            elif target < arr[mid]:
                lower = mid + 1
            elif target == arr[mid]:
                return mid

    return -1  # not found
