def LetterChanges(str): 

    # code goes here 
    
    myList = list(str)
    newList = list('')
	
    for letter in myList:
	
        if letter.isalpha():
            newChar = chr(ord(letter)+1)
            if newChar in ('a','e','i','o','u'):
                newChar = newChar.upper()
            newList.append(newChar)
			
        else:
            newList.append(letter)
    
    #print(''.join(newList))
    
    str = ''.join(newList)
    
    
    return str
    
# keep this function call here  
print LetterChanges(raw_input())