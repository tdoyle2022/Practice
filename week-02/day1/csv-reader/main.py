import csv
import re
# try:
userinpt = input('Type of animal: ')
if userinpt == 'dogs':
    with open('data/dogs.csv', newline='') as csvfile:
            dogreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in dogreader:
                [' '.join(row)]
                print(f"{row[0]} is a {row[1]} year old {row[2]}")
                # print(re.sub(',','', sen))
if userinpt == 'cats':
    with open('data/cats.csv', newline='') as csvfile:
            catreader = csv.reader(csvfile, delimiter=', ', quotechar='|')
            for row in catreader:
                [' '.join(row)]
                print(f"{row[0]} is a {row[1]} year old {row[2]}")
                # print(re.sub(',','',sen2))
elif userinpt != 'cats' or 'dogs':
     print(f"Sorry, we don't have any {userinpt} here.")
# except Exception as e:
#     if userinpt != 'dogs' or 'cats':
#         print(f"Sorry, we don't have any {userinpt} here.")