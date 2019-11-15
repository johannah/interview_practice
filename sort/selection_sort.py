# O(n^2)

def find_min_index(array):
    min_value = array[0]
    min_index = 0 
    for i, val in enumerate(array[1:]):
        if val < min_value:
            min_value = val 
            min_index = i+1
    return min_index

def selection_sort(array):
    for i in range(0, len(array)-1):
        min_index = i+find_min_index(array[i:])
        min_val = array[min_index]
        array[min_index] = array[i]
        array[i] = min_val
    return array

for arr in [[3,5,1,10,0], [33,333342,3,-99,31,-192]]:
    sarr = selection_sort(arr)
    print(sarr)
    assert(sarr == sorted(arr))

