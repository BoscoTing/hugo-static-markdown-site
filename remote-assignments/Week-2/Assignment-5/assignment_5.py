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
