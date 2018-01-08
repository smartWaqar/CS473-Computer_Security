from operator import xor
from binascii import a2b_base64
from binascii import b2a_hex
import os.path
from decimal import *



#Take a string and an integer(key) and take xor of key with every byte of inputString and return it
def singleByteXor_withInt(inputString, key):         
    tempString = inputString
    finalString = ""
    for i in range(0,len(inputString)/2):
        tempChunk = tempString[0:2]
        tempString = tempString[2:]
        xorResult = xor(int(tempChunk,16),key)
        finalChunk = "{0:x}".format(xorResult)
        if (len(finalChunk) == 1):
            finalChunk = "0"+ finalChunk
        #finalChunk = chr(int(finalChunk,16))
        finalString += finalChunk
    
    #if len(finalString) %2 != 0:
        #finalString += "0"
    return finalString
    
# Score a string based upon its character frequency. Dictionary taken online
def scoreString(inputString):
    freq = dict()
    freq['a']=834
    freq['b']=154
    freq['c']=273
    freq['d']=414
    freq['e']=1260
    freq['f']=203
    freq['g']=192
    freq['h']=611
    freq['i']=671
    freq['j']=23
    freq['k']=87
    freq['l']=424
    freq['m']=253
    freq['n']=680
    freq['o']=770
    freq['p']=166
    freq['q']=9
    freq['r']=568
    freq['s']=611
    freq['t']=937
    freq['u']=285
    freq['v']=106
    freq['w']=234
    freq['x']=20
    freq['y']=204
    freq['z']=6
    freq[' ']=2320
  
    score = 0
    for character in inputString.lower():
        if character in freq:
            score += freq[character]
        
    return score
    
    
    


def p1():
    #print "------------- Problem 1 ----------------- \n"
    s = raw_input("Enter hex string: ")
    s = s.decode("hex")
    print s
    s = s.encode("base64")
    print "Base 64 string: ", s, "\n"
    
    
def p2():
    #print "------------ Problem 2 --------------------\n"
    s1 = raw_input("Enter first hex string:  ")
    s2 = raw_input("Enter second hex string: ")
    #s1 = "1c0111001f010100061a024b53535009181c"
    #s2 = "686974207468652062756c6c277320657965"
    #s1 = s1.decode("hex")
    #s2 = s2.decode("hex")
    #print s1
    #print s2
    s1 = int(s1,16)
    s2 = int(s2,16)
    s = xor(s1,s2)
    print format(s, '02x')
    
    



def p3(inputString):
    #print "------------ Problem 3 --------------------\n"
    #inputString = raw_input("Enter hex String")
    #inputString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    
    finalString = ""
    finalScore = 0
    finalKey = 0
    for i in range(41,128):
        charInByteString = str("{0:x}".format(i))
        if len(charInByteString) == 1:
            charInByteString  = "0"+ charInByteString
        tempString = charInByteString*(len(inputString)/2)
        #print len(tempString), "     ", tempString
        
        xorResult = xor(int(inputString,16),int(tempString,16))
        xorString = "{0:x}".format(xorResult)
        if len(xorString)%2 == 1:
            xorString = "0"+ xorString
        iString = xorString.decode('hex')
        #print i, "  ", iString,"  ",scoreString(iString)
        score_iString = scoreString(iString)
        if score_iString > finalScore:
            finalString = iString
            finalScore = score_iString
            finalKey = i
            
    #print finalString," " , chr(finalKey)
    return finalString
    
def p3_key(inputString):
    #print "------------ Problem 3 --------------------\n"
    #inputString = raw_input("Enter hex String")
    #inputString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    
    finalString = ""
    finalScore = 0
    finalKey = 0
    for i in range(41,128):
        charInByteString = str("{0:x}".format(i))
        if len(charInByteString) == 1:
            charInByteString  = "0"+ charInByteString
        tempString = charInByteString*(len(inputString)/2)
        #print len(tempString), "     ", tempString
        
        xorResult = xor(int(inputString,16),int(tempString,16))
        xorString = "{0:x}".format(xorResult)
        if len(xorString)%2 == 1:
            xorString = "0"+ xorString
        iString = xorString.decode('hex')
        #print i, "  ", iString,"  ",scoreString(iString)
        score_iString = scoreString(iString)
        if score_iString > finalScore:
            finalString = iString
            finalScore = score_iString
            finalKey = i
            
    #print finalString," " , chr(finalKey)
    return chr(finalKey)

def p4():
    myfile = open("4.txt",'r')
    inString = myfile.readline()
    inString = inString.replace("\n","")
    
    finalString = ""
    finalScore = 0
    while inString:
        #print inString, len(inString)
        tempString = p3(inString).replace("\n","")
        tempScore  = scoreString(tempString)
        if (finalScore < tempScore):
            finalScore = tempScore
            finalString = tempString
        #print p3(inString)
        inString = myfile.readline()
        inString = inString.replace("\n","")
        
    print finalString
    
def string_to_hexString(inputString):
    finalString = ""
    for character in inputString:
        temp = "{0:x}".format(ord(character))
        if ( len(temp) == 1):
            temp = "0" + temp
        finalString += temp
    return finalString
    
def applyRepeatingKeyXor(inputString,xorString):
    len_inputString = len(inputString)
    len_xorString = len(xorString)
    final_xorString = xorString*(len_inputString / len_xorString)
    final_xorString += xorString[0:len_inputString % len_xorString]
    
    inputString = string_to_hexString(inputString)
    final_xorString = string_to_hexString(final_xorString)
    resultString  = xor( int(inputString,16), int(final_xorString,16) ) 
    resultString = "{0:x}".format(resultString)
    if (len(resultString) != len(inputString)):
        resultString = "0" + resultString
    

    #print inputString
    #print final_xorString
    #print resultString, len(resultString)
    return resultString
    

def p5(fileName, key):
    #fileName = raw_input("Enter file name: ")
    #fileName = "5.txt"
    myfile = open(fileName,'r')
    outFileName = "enc-" + fileName
    outfile = open( outFileName, 'w+')
    
    mydata = myfile.read()
    #print applyRepeatingKeyXor(mydata,key)
    outfile.write( applyRepeatingKeyXor(mydata,key) )
    
    myfile.close()
    outfile.close()
    
    #inString = myfile.readline()
    #inString = inString#.replace("\n","")
    
    
    #print applyRepeatingKeyXor("Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", "ICE")
    #while inString:
    
        #print applyRepeatingKeyXor(inString, "ICE")
        
        #inString = myfile.readline()
        #inString = inString#.replace("\n","")
    

def HammingDistance(string1, string2):
    hex_string1 = string_to_hexString(string1)
    hex_string2 = string_to_hexString(string2)
    
    bin_string1 = "{0:b}".format(int(hex_string1,16))
    bin_string2 = "{0:b}".format(int(hex_string2,16))
    
    #print hex_string1
    #print hex_string2
    #print bin_string1
    #print bin_string2
    
    
    mydistance = sum(c1 != c2 for c1, c2 in zip(bin_string1, bin_string2))
    #print mydistance
    return mydistance
    
def HammingDistance_hex(string1, string2):
    bin_string1 = "{0:b}".format(int(string1,16))
    bin_string2 = "{0:b}".format(int(string2,16))
    
    mydistance = sum(c1 != c2 for c1, c2 in zip(bin_string1, bin_string2))
    #print mydistance
    return mydistance
    

def normalized_hamming_distance (A, length): 
    ham_sum = 0
    for i in range(len(A)/length - 1):
        ham_sum += HammingDistance(A[(i+0)*length:(i+1)*length], A[(i+1)*length:(i+2)*length])
    ham_avg = (1.0 * ham_sum) / (len(A)/length - 1)
    norm_ham = ham_avg / length
    return norm_ham

#--------------------Block Code Taken From Internet For testing------------------------------------------------
def hamming_distance(A, B):
    X = int(b2a_hex(A),16) ^ int(b2a_hex(B),16)
    return count_binary_ones(X)

def count_binary_ones(X):
    ret = 0
    while X != 0:
        ret = ret + 1
        X &= X-1  
    return ret

def normalized_hamming_distance_2 (A, length): # Takes adjacent groups of 'length' length and finds avg hamming dist and normalizes it
    ham_sum = 0
    for i in range(len(A)/length - 1):
        ham_sum += hamming_distance(A[(i+0)*length:(i+1)*length], A[(i+1)*length:(i+2)*length])
    ham_avg = (1.0 * ham_sum) / (len(A)/length - 1)
    norm_ham = ham_avg / length
    return norm_ham

#-----------------------------------------------------------

def find_KEYSIZE_2(fileName):
    myfile  = open(fileName,'r')
    data = ""
    data = myfile.read()
    
    #for line in open(fileName):
        #data += line.strip()
    data = data.decode("base64")
    #data = string_to_hexString(data)
    #data = a2b_base64(data)
    
    finalKeySize = 2;
    finalScore = 9999999;
    
    for keySize in range(2,41):
        tempScore = normalized_hamming_distance(data,keySize)
        if (finalScore > tempScore):
            finalScore =  tempScore
            finalKeySize = keySize
        print keySize, " - ",  tempScore
        

    print "Final Score: ", finalScore, "   Final Key Size: ", finalKeySize
    return finalKeySize 

def find_KEYSIZE(fileName):
    myfile  = open(fileName,'r')
    data = myfile.read()
    data = data.decode("base64")
    
    data = string_to_hexString(data)
    
    finalKeySize = 2;
    finalScore = 9999999;
    
    for keySize in range(2,40):
        hex_string1 = data[0:keySize*2]
        hex_string2 = data[keySize*2:keySize*4]
        hex_string3 = data[keySize*4:keySize*6]
        hex_string4 = data[keySize*6:keySize*8]
        hex_string5 = data[keySize*8:keySize*10]

        ham_distance1 = HammingDistance_hex(hex_string1, hex_string2)
        ham_distance2 = HammingDistance_hex(hex_string2, hex_string3)
        ham_distance3 = HammingDistance_hex(hex_string3, hex_string4)
        ham_distance4 = HammingDistance_hex(hex_string4, hex_string5)

        ham_distance = ( ham_distance1 + ham_distance2 + ham_distance3 + ham_distance4 )/4
        tempScore = Decimal(ham_distance)/keySize
        if (finalScore > tempScore):
            finalScore =  tempScore
            finalKeySize = keySize
        print keySize, "  ",  tempScore
        

    #print "Final Score: ", finalScore, "   Final Key Size: ", finalKeySize
    return finalKeySize        
    
def p6(fileName):
    
    #data = ""
    myfile = open(fileName, 'r')
    data = myfile.read()
    #for line in open(fileName):
    #    data += line.strip()
    data = data.decode('base64')
    data = string_to_hexString(data)
    
    keySize = find_KEYSIZE_2(fileName)
    """
    data_blocks = [""] * keySize
    #print data
    key = ""
    finalData = ""
    
    tempData = data
    for i in range(0, len(data)/2):
        tempByte = tempData[0:2]
        tempData = tempData[2:]
        
        data_blocks[(i % keySize)] += tempByte
        
    for i in range(0, keySize):
        finalData += p3(data_blocks[i])
        key += p3_key(data_blocks[i])
        
    print "---------------- Final Data ------------------"
    print finalData
    print "------------ key ---------------"
    print key
    
    data_blocks = [""] * keySize
    #print data
    key = ""
    finalData = ""
    """
    
    
    for keySize in range(2, 40):
        print "------------------- ", keySize , "--------------------\n"
        data_blocks = [""] * keySize
        #print data
        key = ""
        finalData = ""
        finalData2 = [""] * keySize
        tempData = data
        for i in range(0, len(data)/2):
            tempByte = tempData[0:2]
            tempData = tempData[2:]
        
            data_blocks[(i % keySize)] += tempByte
        
        for i in range(0, keySize):
            finalData += p3(data_blocks[i])
            finalData2[i] = p3(data_blocks[i])
            key += p3_key(data_blocks[i])
        
        finalData3 = ""    
        min_len_str = len(min(finalData2, key=len))
        for i in range(0, min_len_str):
            for j in range(0, keySize):
                finalData3 += finalData2[j][i]
        
        print "---------------- Final Data ------------------"
        #print finalData
        print finalData3
        print "------------ key ---------------"
        print key, "\n"
    
    
def p7(fileName, key):
    #print "---------- Problem 7 ------------------------"
    from Crypto.Cipher import AES
    obj = AES.new(key, AES.MODE_ECB)
    
    
    myfile = open(fileName, 'r')
    outfile = open('dec-' + fileName, 'w+')
    
    data = myfile.read()
    data = data.decode('base64')
    
    decryptedText = obj.decrypt(data)
    outfile.write(decryptedText)
    
    myfile.close()
    outfile.close()

def detect_rep_ECB_128 (inputString):
    """ detect repetition in hex string for AES """
    
    tempString = inputString
    numChunks = len(inputString)/32
    chunkArray = [""] * numChunks
    
    for i in range(0, numChunks):
        temp = tempString[0:32]
        tempString = tempString[32:]
        chunkArray[i] = temp
        
    for i in range(0,len(chunkArray)):
        if chunkArray[i] in chunkArray[i+1:]:
            return True
            
    return False
    

def p8(fileName):
    myfile = open(fileName,'r')
    
    sString = myfile.readline()
    
    while (sString):
        
        #print sString
        #print sString.decode('hex')
        myresult = detect_rep_ECB_128(sString)
        if (myresult == True):
            print sString
        
        sString = myfile.readline()



def main():
    
    getcontext().prec = 10
    
    print "Uncomment Problem Functions to run them!"
    
    #p1()
    #p2()
    #inputString = raw_input("Enter hex String: ")
    #print p3(inputString)
    #p4()
    #p5("5.txt", "ICE")
    
    #HammingDistance("this is a test","wokka wokka!!!")
    #find_KEYSIZE_2("6.txt")
    print "Problem 6 is brute Forced on all key lengths"
    #p6("6.txt")
    

    
    #p7("7.txt", "YELLOW SUBMARINE")
    #p8('8.txt')







if __name__ == "__main__":
    """s1 = "this is a test"
    s2 = "wokka wokka!!!"
    #s1 = string_to_hexString(s1)
    #s2 = string_to_hexString(s2)
    
    print HammingDistance(s1,s2);
    print normalized_hamming_distance(s1+s2,14)
    if HammingDistance(s1, s2) == 37:
        print "Hamming Distance tests pass"
    if normalized_hamming_distance(s1+s2,14) == 37.0/14:
        print "Normalized Hamming Distance tests pass"
    #else:
        #print normalized_hamming_distance(s1+s2,14)"""
    main()


