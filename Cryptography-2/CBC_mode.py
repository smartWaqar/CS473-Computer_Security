
from repeatingKeyXor import *
from ECB_mode import *
from PKCS_padding import *

def CBC_encrypt(plainData, key, iv):
    
    tempData = plainData
    if len(plainData) % 16 != 0:
        plainData = PKCS_padding(plainData, (len(plainData)/16 + 1)*16)
    numDataBlocks = int(len(plainData)/16)
    encryptedData = ""
    
    encrypted_block = ""
    for i in range(0,numDataBlocks):
        tBlock = tempData[0:16]
        tempData = tempData[16:]
        #tBlock = string_to_hexString(tBlock)
        if (i == 0):
            xored_block = repeatingKeyXor(tBlock,iv)
            xored_block = xored_block.decode('hex')
            encrypted_block = ECB_encrypt(xored_block,key)
            encrypted_block = encrypted_block.decode('base64')
            encryptedData += encrypted_block
        else:
            #print "I", len(xored_block), len(key), len(tBlock)
            xored_block = repeatingKeyXor(encrypted_block,tBlock)
            if len(xored_block) % 2 ==1:
                xored_block = "0" + xored_block
            #print len(xored_block)
            xored_block = xored_block.decode('hex')
            
            #print "I", len(xored_block), len(key), len(tBlock), "------"
            
            encrypted_block = ECB_encrypt(xored_block,key)
            encrypted_block = encrypted_block.decode('base64')
            encryptedData += encrypted_block
    
    encryptedData = encryptedData.encode('base64')    
    return encryptedData        
    

"""            
key = "YELLOW SUBMARINE"
iv  = "\\x00\\x00\\x00\\x00"
myfile = open("10.txt")
data = myfile.read()
print CBC_encrypt(data,key,iv)
"""    