def binary_search(array, search, min_idx, max_idx):
    guess_idx = min_idx + (max_idx-min_idx)//2
    # assume array is sorted
    assert array[0] <= search <= array[-1]
    if search == array[guess_idx]:
        print('found', array[guess_idx])
        return guess_idx
    elif search < array[guess_idx]:
        return binary_search(array, search, min_idx, guess_idx)
    else:
        return binary_search(array, search, guess_idx, max_idx)


arr = [0,2,5,6,7,20,80,1000]
for d in arr:
    assert(binary_search(arr, d, 0, len(arr)) == arr.index(d))

