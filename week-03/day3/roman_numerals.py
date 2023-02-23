def to_num(num):
    new_num = ""
    numerals = {
        "M": 1000,
        "IM": 999,
        "VM": 995,
        "XM": 990,
        "LM": 950,
        "CM": 900,
        "D": 500,
        "ID": 499,
        "VD": 495,
        "XD": 490,
        "LD": 450,
        "CD": 400,
        "C": 100,
        "IC": 99,
        "VC": 95,
        "XC": 90,
        "L": 50,
        "IL": 49,
        "VL": 45,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1}
    for i in numerals:
        if num >= numerals[i]:
            new_num += i
            num -= numerals[i]
            return new_num + to_num(num)
    return new_num
print(to_num(1550))


# def roman(n):
#   """Takes a roman number n as an argument 
#      (roman(n) assumes that the string n is 
#      correctly written, i.e. it provides no 
#      error-checking) and returns an integer."""

#   #The base-cases:

#   if n == "":
#     return 0
#   elif n == "M":
#     return 1000
#   elif n == "D":
#     return 500
#   elif n == "C":
#     return 100
#   elif n == "L":
#     return 50
#   elif n == "X":
#     return 10
#   elif n == "V":
#     return 5
#   elif n == "I":
#     return 1

#   #If a smaller number precedes a bigger number, 
#   #then the smaller number is to be subtracted from 
#   #the bigger number. Else, it has to be added:

#   else:
#     if roman(n[0]) < roman(n[1]):
#       return (roman(n[1]) - roman(n[0])) + roman(n[2:])
#     else:
#       return roman(n[0]) + roman(n[1:])

# def main(n): 
#   print(roman(n))

# main("MMMCMXCIX")
