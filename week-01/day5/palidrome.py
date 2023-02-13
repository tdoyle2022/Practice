def palidrome(word):
    if type(word) == str and word[::-1] == word:
        return True
    elif type(word) == int and join(str(word).split('').reverse()) == word:
        print(word)
        return True
    else:
        return False
    

print(palidrome(1221))