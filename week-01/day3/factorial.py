def factorial(num):
    lst = []
    answer = 1
    if num == 0 | num == 1:
        return 1
    for x in range(1, num+1):
        lst.append(x)
    for number in lst:
        answer *= number
    return print(answer)  
factorial(5)


    