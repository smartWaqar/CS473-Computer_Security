

def detect_ECB (inputString):
    """ detect repetition in hex string for AES """
    
    tempString = inputString
    numChunks = len(inputString)/32
    chunkArray = [""] * numChunks
    
    for i in range(0, numChunks):
        temp = tempString[0:32]
        tempString = tempString[32:]
        chunkArray[i] = temp
        
    #print chunkArray
    
    for i in range(0,len(chunkArray)):
        if chunkArray[i] in chunkArray[i+1:]:
            return True
            
    return False
    


