def LongestWord(sen): 

    # code goes here 
    
    words = sen.split(' ')
    
    longestWord = ''
    longestWordLength = 0
    
    
    for word in words:
        
        newWord = ''
        for myChar in word:
            if myChar.isalpha():
                newWord = newWord + myChar
        
        if len(newWord) > longestWordLength:
            longestWord = newWord
            longestWordLength = len(newWord)
    
    
    return longestWord
    
# keep this function call here  
print LongestWord(raw_input())