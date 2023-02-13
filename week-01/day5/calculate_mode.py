def calculate_mode(lst):
    answer = []
    dict = {}
    frequency = 0
    for num in lst:
        count = lst.count(num)
        dict[num] = count
        if count > frequency:
            frequency = count
    for key in dict:
        if dict[key] == frequency:
            answer.append(key)
    return answer

print(calculate_mode([1,2,2,2,3,4,5,7]))