sequence = [4,3,5,0,1]
swaps = 0

def bubble_sort(lst):
    counter = len(lst)
    global swaps
    while counter > 0:
        for i in range(len(lst)-1):
            first = lst[i]
            second = lst[i+1]
            if first > second:
                temp = second
                lst[i+1] = first
                lst[i] = temp
                swaps += 1
        counter -= 1
    return lst
print(bubble_sort(sequence))
print(f"Swaps: {swaps}")