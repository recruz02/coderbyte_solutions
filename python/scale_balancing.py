def ScaleBalancing(strArr): 


    # clean data and separtae into proper tuples
    
    myVals = list(strArr)
    
    myString1 = myVals[0]
    myString1 = myString1.replace('[','')
    myString1 = myString1.replace(']','')
    myString1 = myString1.replace(' ','')
    #print(myString1)

    myString2 = myVals[1]
    myString2 = myString2.replace('[','')
    myString2 = myString2.replace(']','')
    myString2 = myString2.replace(' ','')
    #print(myString2)

    scale = myString1.split(',')       #ex: [3,4]
    #print(scale)
    
    weights = myString2.split(',')     #ex: [1,2,7,7]
    #print(weights)
    
    

    # Scenario1: Try adding one weight to either side for balance
    for position in range(0, len(weights)):
        
        #print(scale[0] + weights[position])
        
        if int(scale[0]) + int(weights[position]) == int(scale[1]):
            return weights[position]
        elif int(scale[1]) + int(weights[position]) == int(scale[0]):
            return weights[position]
        
        

    for leftPosition in range(0, len(weights)):
        
        for rightPosition in range(0, len(weights)):
            #ignore when positions are equal
          
            # Scenario2a: Try adding one of each weight to each side  
            if (
                    leftPosition != rightPosition and 
                    leftPosition < rightPosition and
                    (int(scale[0]) + int(weights[leftPosition])) == (int(scale[1]) + int(weights[rightPosition]))
                ):
                    
                return str(int(weights[leftPosition])) + "," + str(int(weights[rightPosition]))

            # Scenario2b: Try adding one of each weight to each side (flippy floppy)
            if (
                    leftPosition != rightPosition and 
                    leftPosition > rightPosition and
                    (int(scale[0]) + int(weights[leftPosition])) == (int(scale[1]) + int(weights[rightPosition]))
                ):
                    
                return str(int(weights[rightPosition])) + "," + str(int(weights[leftPosition]))


            # Scenario 3: Try adding two weights to left side
            elif (
                    leftPosition != rightPosition and 
                    (int(scale[0]) + int(weights[leftPosition])) + int(weights[rightPosition]) == int(scale[1])
                ):
                    
                return str(int(weights[leftPosition])) + "," + str(int(weights[rightPosition]))

            # Scenario 4: Try adding two weights to righte side
            elif (
                    leftPosition != rightPosition and 
                    int(scale[0]) == int(scale[1]) + int(weights[rightPosition]) + int(weights[leftPosition])
                ):
                    
                return str(int(weights[leftPosition])) + "," + str(int(weights[rightPosition]))
    


    # code goes here 
    return "not possible"
    
# keep this function call here  
print ScaleBalancing(raw_input())