
# Not Not Not a right method


from detect_ECB import *
from repeatingKeyXor import *



def detect_CBC(data):
    "give hex string "
    cleanedData = remove_CBC_effect(data)
    
    myresult = detect_ECB(cleanedData)
    
    return  myresult
    
    
    
    
def remove_CBC_effect (inputString):
    """ detect repetition in hex string for AES """
    
    tempString = inputString
    numChunks = len(inputString)/32
    chunkArray = [""] * numChunks
    
    for i in range(0, numChunks):
        temp = tempString[0:32]
        tempString = tempString[32:]
        chunkArray[i] = temp
    
    for i in range(0,numChunks):
        chunkArray[i] = chunkArray[i].decode('hex') 
        
    
    mydata = ""
    newChunkArray = []
    for i in range(1,numChunks):
        #chunkArray[i] = repeatingKeyXor(chunkArray[i-1],chunkArray[i]) 
        newChunkArray.append(repeatingKeyXor(chunkArray[i-1],chunkArray[i]))
    
    for i in newChunkArray:
        mydata += i
    return mydata