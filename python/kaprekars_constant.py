def KaprekarsConstant(num): 
    
    
    # CONVERT TO 4-DIGIT NUMBER (sorting will provide minimum); PAD ZEROES
    minString = sorted(str(format(num, '04')))

    
    # REVERSE STRING (to get maximum)
    maxString = minString[::-1]


    # SUBTRACT SMALLER NUMBER FROM LARGER NUMBER
    newNumber = int(''.join(maxString)) - int(''.join(minString))
    

    # VERIFY IF VALUE == 6174
    # IF VALUE != 6174, RECURSIVELY CALL FUNCTION AND INCREASE COUNTER
    if (newNumber == 6174):
        return 1
    else:
        return 1 + KaprekarsConstant(newNumber)

    
# keep this function call here  
print KaprekarsConstant(raw_input())  
