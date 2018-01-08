from string_to_hexString import *
from operator import xor

def repeatingKeyXor(inputString,xorString):
    "----------- Take plain Data and Return hex output------------"
    len_inputString = len(inputString)
    len_xorString = len(xorString)
    final_xorString = xorString*(len_inputString / len_xorString)
    final_xorString += xorString[0:len_inputString % len_xorString]
    
    inputString = string_to_hexString(inputString)
    final_xorString = string_to_hexString(final_xorString)
    resultString  = xor( int(inputString,16), int(final_xorString,16) ) 
    #resultString = string_to_hexString(str(resultString))
    resultString = "{0:x}".format(resultString)
    
    if (len(resultString) != len(inputString)):
        resultString = "0" + resultString

    #if (len(resultString) % 2 == 1):
    #    resultString = "0" + resultString

    #print inputString
    #print final_xorString
    #print resultString, len(resultString)
    return resultString
   
    
"""
tempString = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
print repeatingKeyXor(tempString,key)
"""
