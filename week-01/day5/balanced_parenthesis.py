def is_valid(s):
    
    #Define our bracket pairs via a dictionary
    bracket_pairs = dict(('()', '[]'))
    
    
    #create a empty list to store characters
    list_our = []
    
    
    #for loop to sort through each character in the string
    for this_char in s:
        
        # if statement that looks for brackets
        if this_char in '([{':
            #append any bracket found into our list
            list_our.append(this_char)
            
        #else if the length of our list is equal to 0 OR the character is not of value of our bracket pair then pop it from our list    
        elif len(list_our) == 0 or this_char != bracket_pairs[list_our.pop()]:
            #if the length is 0 then return false. Or if the character is not part of the bracket pair return false
            return False
        
        
    return len(list_our) == 0
    
    
    
    
    
print(is_valid("[]()"))
    