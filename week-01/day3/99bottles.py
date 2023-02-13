def ninety_bottles(num):
    starting_num = num
    while num > 0:
        if num == 1:
            print(f"One bottle of beer on the wall, one bottle of beer. \nTake one down, pass it around, no bottles of beer on the wall. \nNo more bottles of beer on the wall, no more bottles of beer. \nGo to the store and buy some more, {starting_num} bottles of beer on the wall.")
        elif num == 2: 
            print("Two bottles of beer on the wall, two bottles of beer. \nTake one down and pass it around, one bottle of beer on the wall.")
        elif num > 2:
            print(f"{num} bottles of beer on the wall, {num} bottles of beer. \nTake one down and pass it around, {num} bottles of beer on the wall.")
        num -= 1
print(ninety_bottles(1))
