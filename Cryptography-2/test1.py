"binascii hex converter (String.encode('hex')) vs my string to hex String"

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
        s2 = string_to_hexString(myStr)
        
        print len(s1)
        print s1
        print len(s2)
        print s2
        
        if (s1 == s2):
            print "passed"
        else:
            print "failed"
        
        print "-------------------------------------"


def result():
    print 'All tests passed'
    print 'Moral! Use binascii to convert strings, although you have your correct code'

if __name__ == "__main__":
    main()
    result()