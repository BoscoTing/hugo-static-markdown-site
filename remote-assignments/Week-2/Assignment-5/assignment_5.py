def binary_search_first(numbers, 
                        target):
    left = 0
    right = len(numbers)
    while left <= right:
        mid = (left+right) // 2
        if numbers[mid] < target: # 下界
            left += 1
        elif numbers[mid] > target: # 上界
            right -= 1
        else:
            return mid

    return -1

# print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 2)) # should print 1 (the index of the target number ‘2’)
# print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 5)) # should print 2 (the index of the ‘first’ target number ‘5’ shows up)
# print(binary_search_first([1, 2, 5, 5, 5, 6, 7], 3)) # should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)

def bisect_left(a, x, lo=0, hi=None, *, key=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    # Note, the comparison uses "<" to match the
    # __lt__() logic in list.sort() and in heapq.
    if key is None:
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
    else:
        while lo < hi:
            mid = (lo + hi) // 2
            if key(a[mid]) < x:
                lo = mid + 1
            else:
                hi = mid
    return lo

print(bisect_left([1, 2, 5, 5, 5, 6, 7], 3)) # should print 2 (since it can’t find number 3, return the index of ‘the smallest number larger than 3', that is, the index of the ‘first’ number 5)
