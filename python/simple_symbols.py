def SimpleSymbols(pString): 

    # code goes here 
    
    myChars = list(pString)
    
    
    
    for index in range(0, len(myChars)):
        
        # CHECK EDGE CONDITIONS
        if myChars[0].isalpha():
            return "false"
            
        if myChars[len(myChars)-1].isalpha():
            return "false"
        
        # OTHERWISE CHECK LEFT AND RIGHT CHARACTERS
        if myChars[index].isalpha():
            if myChars[index-1] != '+' or myChars[index+1] != '+':
                return "false"
            
    return "true"
    
# keep this function call here  
print SimpleSymbols(raw_input())