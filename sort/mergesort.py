# time complexity O(nlogn) - space complexity O(n)
# use for linked list, - uses a lot of memory for arrays

# divide and conquer algorithm
# 1) divide array into two halves 
# 2) calls itself for the two halves 
# 3) merges the two sorted halves

def mergesort(array):
    if len(array) > 1:
        # find the middle point to divide the array into two halves
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        mergesort(left_array)
        mergesort(right_array)
        i = j = k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i+=1
            else:
                array[k] = right_array[j]
                j+=1
            k+=1
        # if any element was leftover 
        while i < len(left_array):
            array[k] = left_array[i]
            i+=1
            k+=1
        while j < len(right_array):
            array[k] = right_array[j]
            j+=1
            k+=1
    return array

arr = [70,10,-10,1,-500]
print(mergesort(arr))
