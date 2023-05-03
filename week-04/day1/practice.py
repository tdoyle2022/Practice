# split string to form list of pairs with '_' at end if odd string length

# def splitstr(s):
#     if len(s) % 2 != 0:
#         s += "_"
#     return [s[i:i+2] for i in range(0, len(s), 2)]
# print(splitstr('lkdjflkdj'))

def reverse_words(text):
    splttext = text.split()
    for x in splttext:
        return x[::-1]

print(reverse_words('This is an example!'))

