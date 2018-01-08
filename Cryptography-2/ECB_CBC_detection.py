import string
import random
import base64

from ECB_mode import *
from CBC_mode import *

from detect_ECB import *

#---------- My Function ------------------------
def randomString(length):
    myString = ""
    for i in range(0,length):
        tempChar = random.choice(string.ascii_letters + string.digits)
        myString += tempChar
    
    return myString
# -----------------------------------------------

def ECB_CBC_oracle(data):
    
    key = randomString(16)
    iv = randomString(16)
    choice = random.randint(0,1)
    
    print key; print iv; 
    if choice == 0:
        print "ECB encryption"
    else:
        print "CBC encryption"
    
    encryptedData = ""
    if choice == 0:
        encryptedData = ECB_encrypt(data,key)
    else:
        encryptedData = CBC_encrypt(data,key,iv)
    
    #print "Length Encrypted Data: ",len(encryptedData)
    return encryptedData
    
    
def ECB_CBC_detection(data):
    "------ Base 64 input return 0 if ECB else 1 ------------"
    
    #print "Length of Data: ", len(data)

    data = data.decode('base64')
    if len(data) % 2 == 1:
        data = "0" + data
    data = data.encode('hex')
    
    result = detect_ECB (data)
    
    if result == True:
        print "ECB detected"
    else:
        print "CBC detected"
    
    return result


"""
for i in range(0,10):
    data = ECB_CBC_oracle("hello werblopfghYellow Submarinehello werblopfghYellow Submarine")
    ECB_CBC_detection(data)
    print "------------------------------------\n"
    
"""