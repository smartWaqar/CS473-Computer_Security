# Analyze the behaviour of string.encode/encode('base64'/'hex') 

import string
import random

from string_to_hexString import *

def randomString(length):
    myString = ""
    for i in range(0,length):
        tempChar = random.choice(string.ascii_letters + string.digits)
        myString += tempChar
    
    return myString
    

def main():
    
    for i in range(0,30):
        strLength = random.randint(0,100)
        myStr = randomString(strLength)
        
        print "-------------------------------"
        print "Length of my String: ", strLength 
        print "My String: ", myStr
        
        s1 = myStr.encode("hex")
        s2 = myStr.encode("base64")
        s3 = s2.decode('base64')
        
        print "Hex ",len(s1)
        print s1
        print "Base64 ", len(s2)
        print s2
        
        if (s3 == myStr):
            print "passed"
        else:
            print "failed"
        
        print "-------------------------------------"


def result():
    print "Check for the behaviour of base 64 encoding "
    print " "

if __name__ == "__main__":
    main()
    result()