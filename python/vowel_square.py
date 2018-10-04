def isVowel(myChar):
    if myChar in ("a", "e", "i", "o", "u"):
        return True
    else:
        return False



def VowelSquare(strArr): 

    # code goes here 
    
    #print(strArr)
    
    words = list(strArr)
    #print(words[0])
    
    
    for xPosition in range(0, len(words)-1):
        #print(xPosition)
        
        
        for yPosition in range(0,len(words[xPosition])-1):
            #print(words[xPosition][yPosition])
            
            
            if isVowel(words[xPosition][yPosition]):
                #print(isVowel(words[xPosition][yPosition]))
                
                # check other positions for vowels
                if (isVowel(words[xPosition+1][yPosition]) 
                    and isVowel(words[xPosition][yPosition+1]) 
                    and isVowel(words[xPosition+1][yPosition+1])):
                    
                    return str(xPosition) + "-" + str(yPosition)
                    

    return "not found"
    
    
# keep this function call here  
print VowelSquare(raw_input())