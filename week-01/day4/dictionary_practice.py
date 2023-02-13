dict = {}
total_change = 37.23
change_amounts = [100, 50, 20, 10, 5, 1, .25, .10, .05, .01]
for amount in change_amounts:
        while total_change >= amount and total_change > .04:
            print(total_change)
            number = total_change//amount
            value = amount * number
            new_total = round(total_change - number*amount, 2)
            total_change = new_total
            dict[amount] = number 
            
        #     valuelist = list(dict.values())
        # if total_change <= .04:
        #     break
            # print(valuelist)
pennynum = new_total / .01
dict[.01] = pennynum
print(dict)

# string = 'lkdhfkd ljdfj jdlkj'
# splitstr = string.split(' ')
# print(splitstr)

# if len(splitstr) > 2:
#     splitstr.insert(-3, 'and')
# print(splitstr)

# dict = {
#     50: 1,
#     20: 1,
#     10: 3
# }

# answer = ''
# keylist = list(dict.keys())
# for x in keylist:
#     if dict[x] > 1 and (keylist.index(dict[x]) == len(keylist) - 1):
#         answer += f"{int(dict[x])} ${x} bills."
#     elif dict[x] == 1 and (keylist.index(dict[x]) == len(keylist) - 1):
#         answer += f"{int(dict[x])} ${x} bill."
#     elif dict[x] > 1:
#         answer += f"{int(dict[x])} ${x} bills, "
#     elif dict[x] == 1:
#         answer += f"{int(dict[x])} ${x} bill, "
# print(answer)

# if int(dict[.01]) > 1 and total_change <= .04:
        #     varP = f"{int(dict[.01])} pennies."
        # elif int(dict[.01]) > 1 and total_change > .04:
        #     varP = f"and {int(dict[.01])} pennies."
        # elif int(dict[.01]) == 1 and total_change <= .04:
        #     varP = f"{int(dict[.01])} penny."
        # elif int(dict[.01]) == 1 and total_change > .04:
        #     varP = f"and {int(dict[.01])} penny."
            # if 100 in dict:
            #     if int(dict[100]) > 1:
            #         var100 = f"{int(dict[100])} $100 bills "
            #     elif int(dict[100]) == 1:
            #         var100 = f"{int(dict[100])} $100 bill "
            # else:
            #     var100 = ''
            # if 50 in dict:
            #     if int(dict[50]) > 1:
            #         var50 = f"{int(dict[50])} $50 bills, "
            #     elif int(dict[50]) == 1:
            #         var50 = f"{int(dict[50])} $50 bill, "
            # else:
            #     var50 = ''
            # if 20 in dict:
            #     if int(dict[20]) > 1:
            #         var20 = f"{int(dict[20])} $20 bills, "
            #     elif int(dict[20]) == 1:
            #         var20 = f"{int(dict[20])} $20 bill, "
            # else:
            #     var20 = ''
            # if 10 in dict:
            #     if int(dict[10]) > 1:
            #         var10 = f"{int(dict[10])} $10 bills, "
            #     elif int(dict[10]) == 1:
            #         var10 = f"{int(dict[10])} $10 bill, "
            # else:
            #     var10 = ''
            # if 5 in dict:
            #     if int(dict[5]) > 1:
            #         var5 = f"{int(dict[5])} $5 bills, "
            #     elif int(dict[5]) == 1:
            #         var5 = f"{int(dict[5])} $5 bill, "
            # else:
            #     var5 = ''
            # if 1 in dict:
            #     if int(dict[1]) > 1:
            #         var1 = f"{int(dict[1])} $1 bills, "
            #     elif int(dict[1]) == 1:
            #         var1 = f"{int(dict[1])} $1 bill, "
            # else:
            #     var1 = ''
            # if .25 in dict:
            #     if int(dict[.25]) > 1:
            #         varQ = f"{int(dict[.25])} quarters, "
            #     elif int(dict[.25]) == 1:
            #         varQ = f"{int(dict[.25])} quarter, "
            # else:
            #     varQ = ''
            # if .10 in dict:
            #     if int(dict[.10]) > 1:
            #         varD = f"{int(dict[.10])} dimes, "
            #     elif int(dict[.10]) == 1:
            #         varD = f"{int(dict[.10])} dime, "
            # else:
            #     varD = ''
            # if .05 in dict:
            #     if int(dict[.05]) > 1:
            #         varN = f"{int(dict[.05])} nickles, "
            #     elif int(dict[.05]) == 1:
            #         varN = f"{int(dict[.05])} nickle, "
            # else:
            #     varN = ''
            # if .01 in dict:
            #     if int(dict[.01]) > 1 and total_change <= .04:
            #         varP = f"{int(dict[.01])} pennies."
            #     elif int(dict[.01]) > 1 and total_change > .04:
            #         varP = f"and {int(dict[.01])} pennies."
            #     elif int(dict[.01]) == 1 and total_change <= .04:
            #         varP = f"{int(dict[.01])} penny."
            #     elif int(dict[.01]) == 1 and total_change > .04:
            #         varP = f"and {int(dict[.01])} penny."
            # else:
            #     varP = ''     
            # answer = openingstr + var100 + var50 + var20 + var10 + var5 + var1 + varQ + varD + varN + varP