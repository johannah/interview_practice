# worst case O(n^2)
# good case O(n)

def insertion_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i -1
        while (j>=0 and array[j]>key):
            # scoot
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array

arr = [3,-9,5, 100,-2, 294,5,56]
sarr = insertion_sort(arr)
print(sarr, sorted(arr))
assert(sarr == sorted(arr))
