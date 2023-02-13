def fibonacci(num):
    lst = [0,1]
    count = 0
    first = 0
    second = 1
    while num >= count:
        temp = first + second
        first = second
        second = temp
        lst.append(temp)
        count = count + 1
        
