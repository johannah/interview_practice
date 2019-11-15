# O(n log n)  - low memory requirement. prefer for contiguous arrays, but choose mergesort for linked list
# 1) pick XX element as pivot
# 2) partition the array around the picked pivot 
#  def partition() given an array and an element x of array as pivot - put x at its correct position in sorted array and put all smaller elements before x, all larger elements after x (done in linear time)

def partition(array, low, high):
    i = low-1
    pivot = array[high]
    for j in range(low, high):
        if array[j] < pivot:
            i+=1
            array[i], array[j] = array[j], array[i]
    pi = i+1
    array[pi], array[high] = array[high], array[pi]
    return pi, array

def quicksort(array, low=None, high=None):
    if low == None:
        low = 0
    if high == None:
        high = len(array)-1
    if low < high:
         # pi is parittioning index, array[pi] is at correct place
         pi, array = partition(array, low, high)
         array = quicksort(array, low, pi-1)
         array = quicksort(array, pi+1, high)
    return array

arr = [2354,2,35,-22,34,2,344]
sarr = quicksort(arr)
print(sarr)
assert sarr == sorted(arr)
