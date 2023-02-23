def palindrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        if string[0] == string[len(string) - 1]:
            new_string = string[1:-1]
            print(new_string)
            return palindrome(new_string)
        else: return False
print(palindrome("racecar"))

# def palindrome(string, start, end):
#     if start == end:
#         return True
#     if string[start] != string[end]:
#         return False
#     if start < end +1:
#         return palindrome(string, start + 1, end +1)
#     return True