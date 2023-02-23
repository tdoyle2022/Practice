

def search(lst, n):

    lower_pointer = 0
    upper_pointer = len(lst) - 1

    while lower_pointer <= upper_pointer:
        midpoint = lower_pointer + (upper_pointer - lower_pointer) // 2
        midpoint_value = lst[midpoint]
        if midpoint_value == n:
            return midpoint
        
        elif n < midpoint_value:
            upper_pointer = midpoint - 1
        else:
            lower_pointer = midpoint + 1
    return None
print(search([1,2,5,7,8,9], 8))


