
def binary_search(num, lst):
    mid = len(lst)//2
    if lst[mid] == num:
        return mid

    elif num > lst[mid]:
        print(lst[:mid])
        return mid + binary_search(num,lst[mid:])


    elif num < lst[mid]:
        print(lst[:mid])
        return binary_search(num,lst[:mid])
    
print(binary_search(9, [1, 3, 6, 9, 24, 53, 67, 99]))