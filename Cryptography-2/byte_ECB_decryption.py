import string
import random
import base64

from ECB_mode import *
from CBC_mode import *

from detect_ECB import *


def randomString(length):
    myString = ""
    for i in range(0,length):
        tempChar = random.choice(string.ascii_letters + string.digits)
        myString += tempChar
    
    return myString


key = randomString(16)
unknown_data_b64 = """ Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
YnkK"""

unknownData = unknown_data_b64.decode('base64')

def ECB_fixed_oracle(data):
    encryptedData = ECB_encrypt(data,key)
    return encryptedData

def detect_blockSize(fixed_oracle):
    myString = "A"
    encryptedData = fixed_oracle(myString)
    smallestBlockLength = len(encryptedData.decode('base64'))
    
    for i in range(2,2000):
        tempString = myString * i
        encryptedData = fixed_oracle(tempString)
        tempLength = len(encryptedData.decode('base64'))
        if tempLength % smallestBlockLength == 0:
            return smallestBlockLength
        
        return -1
    
def byte_ECB_decryption(fixed_oracle, data):
    
    #decoyString = ""
    decoyString = "A" * 32
    encData = fixed_oracle(decoyString + data)
    encData =   encData.decode('base64').encode('hex')
    
    blockSize = detect_blockSize(fixed_oracle)
    check_ECB = detect_ECB(encData)
    
    if check_ECB == False:
        return -1
     
    finalData = ""
    
    for byteData in data:
    
        myString = "A" * blockSize
        myStrLength = len(myString)
    
        #print blockSize;print check_ECB;print dataLength
        
        bytesFound = 0
        asciiRange = 256
        
        iterString = myString[0:len(myString)-1]
        
        
        encStrCombArray = [""] * asciiRange
        
        for k in range(0,asciiRange):
            
            tempStr = iterString + chr(k)
            #print tempStr
            tempEnc_b64 = fixed_oracle(tempStr + byteData)
            tempEnc_hex = tempEnc_b64.decode('base64').encode('hex')
            tempEnc_hex = tempEnc_hex[0:myStrLength*2 - 6]
            #print len(tempEnc_hex)
        
            encStrCombArray[k] = tempEnc_hex
            
            iterEnc_b64 = fixed_oracle(iterString + byteData)
            iterEnc_hex = iterEnc_b64.decode('base64').encode('hex')
            iterEnc_hex = iterEnc_hex[0:myStrLength*2 - 6]
        
    
        
        
        #print "Iter String Length: ", len(iterString)
        #print "Array element length: ", len(encStrCombArray[0])
        
        
        #for i in encStrCombArray:
        #    print i
        
        #print "------------------------------------ \n"    
        #print iterEnc_hex
    
        myByte_hex = encStrCombArray.index(iterEnc_hex)
        finalData += chr(myByte_hex)
        #print myByte_hex    
        #print repr(finalData)
        
    return finalData
    
   
def main():

    enc_unknown_data = ECB_fixed_oracle(unknownData)
    #enc_unknown_data = enc_unknown_data.decode('base64')
    
    print enc_unknown_data

    enc_unknown_data = ECB_fixed_oracle("AAAAAAAA"+ "AAAAAAAA"+unknownData)
    #enc_unknown_data = enc_unknown_data.decode('base64')
    
    print enc_unknown_data
    
    
    enc_unknown_data = ECB_fixed_oracle("AAAAAAAA" + "AAAAAAAA")
    print enc_unknown_data

    enc_unknown_data = ECB_fixed_oracle("AAAAAAAA" + "AAAAAAAA" + "AAAAAAAA" + "AAAAAAAA")
    print enc_unknown_data
    
    
    #print byte_ECB_decryption(ECB_fixed_oracle, enc_unknown_data)
    
    #print ECB_fixed_oracle(unknown_data)

    



if __name__ == "__main__":
    main()
    