def LetterCapitalize(str): 

    # code goes here 
    words = str.split(' ')
    
    for index in range(0,len(words)):
        words[index] = words[index][0].upper() + words[index][1::]
    
    return (' '.join(words))
    
# keep this function call here  
print LetterCapitalize(raw_input())
