from binascii import b2a_base64
from PKCS_padding import *

#------ function decrypt accept data in base 64 -----------------

def ECB_decrypt(cipherData, key):
    from Crypto.Cipher import AES
    obj = AES.new(key, AES.MODE_ECB)
    
    data = cipherData.decode('base64')
    
    decryptedText = obj.decrypt(data)
    return decryptedText
    
def ECB_encrypt(plainData, key):
    "------------ Plain Data to Base 64 -----------------"
    from Crypto.Cipher import AES
    obj = AES.new(key, AES.MODE_ECB)
    
    if len(plainData) % 16 != 0:
        plainData = PKCS_padding(plainData, (len(plainData)/16 + 1)*16)
    
    data = plainData
    if len(data)%2  == 1:
        data = "0" + data
    
    encryptedText = obj.encrypt(data)
    
    return b2a_base64(encryptedText)
    
  
"""
myfile = open("7.txt", 'r')
data = myfile.read()
key = "YELLOW SUBMARINE"
data =  ECB_decrypt(data,key)
data = ECB_encrypt(data,key)
print ECB_decrypt(data,key)
"""



