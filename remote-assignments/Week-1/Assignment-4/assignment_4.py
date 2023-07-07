def binary_search_position(numbers, 
                           target):
    if target in numbers:
        left = 0
        right = len(numbers)
        while left <= right:
            mid = int((left+right) / 2)
            if numbers[mid] < target: 
                left += 1
            elif numbers[mid] > target:
                right -= 1
            else:
                return mid
    else: 
        return -1

print(binary_search_position([1, 2, 5, 6, 7], 1)) # should print 0 
print(binary_search_position([1, 2, 5, 6, 7], 6)) # should print 3
print(binary_search_position([1, 2, 5, 6, 7], 9))