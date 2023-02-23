def ninety_nine_bottles(num):
    if num <= 2:
        print(f'{num} bottles of beer on the wall, {num} bottles of beer, take one down, pass it around, {num - 1} bottle of beer on the wall.')
    elif num > 2:
        print(f'{num} bottles of beer on the wall, {num} bottles of beer, take one down, pass it around, {num - 1} bottles of beer on the wall.')
        ninety_nine_bottles(num - 1)


print(ninety_nine_bottles(99))