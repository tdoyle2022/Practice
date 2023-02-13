
def count_letters(word1, word2):
    dict = {}
    dict2 = {}
    for letter in word1:
        if letter not in dict:
            dict[f'{letter}'] = 1
        else:
            dict[f'{letter}'] += 1
    for letter in word2:
        if letter not in dict:
            dict[f'{letter}'] = 1
        else:
            dict[f'{letter}'] += 1



print(count_letters(["cognac", "saltier", "realist", "retails"]))
