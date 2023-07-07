def binary_search_position(numbers, 
                           target):
    left = 0
    right = len(numbers)
    while left < right:
        mid = (left+right) // 2
        if numbers[mid] < target: 
            left += 1
        elif numbers[mid] > target:
            right -= 1
        else:
            return mid
    return -1