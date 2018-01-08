
def PKCS_padding(inputString, mylength):
    len_pad = mylength - len(inputString)
    finalString = inputString + (chr(len_pad) * len_pad )
    #print chr(len_pad) * len_pad
    return finalString
    

    
#print len(PKCS_padding("Yellow Submarine",20))
#print repr(PKCS_padding("Yellow Submarine", 20))
    

    


