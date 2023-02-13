def deaf_grandma():
    words = input('')
    counter = 0
    while counter <= 2:
        if words == 'GOODBYE!' and counter == 0:
            print("LEAVING SO SOON?")
            counter += 1
            words = input('')
        elif words == 'GOODBYE!' and counter != 0:
            print('LATER SKATER!')
            break
        elif words == (''):
            print("WHAT?!")
            words = input('')
            counter = 0
        elif words == words.upper():
            print("NO, NOT SINCE 1946!")
            words = input("")
            counter = 0
        elif words != words.upper():
            print("SPEAK UP, KID!")
            words = input('')
            counter = 0

deaf_grandma()