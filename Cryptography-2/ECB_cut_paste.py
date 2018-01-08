import json

from byte_ECB_decryption import *

def cookieParser(inputStr):
    #inputStr = inputStr.replace('&',',')
    #inputStr = inputStr.replace('=',':') 
    partsArray = inputStr.split("&")
    resultDict = {}
    #print partsArray
    #print inputStr
    for i in partsArray:
        tempArray = i.split('=')
        resultDict[tempArray[0]] = tempArray[1]
        
    jsonObj = json.dumps(resultDict)
    return jsonObj
    
def cookie_reverseParser(inputStr):
    myDict = json.loads(inputStr)
    resultStr = ""
    for i in myDict:
        resultStr += i + "="
        resultStr += str(myDict[i]) + "&"
        
    return resultStr[:-1]
        

    
def profile_for(inputStr):
    inputStr = inputStr.replace('&', '')
    inputStr = inputStr.replace('=', '')

    resultDict = {}
    resultDict["email"] = inputStr
    resultDict["uid"] = 10
    resultDict["role"] = "user"
    
    #resultStr = "email=" + inputStr + "&uid=10" + "&role=user"  
    
    myObj = json.dumps(resultDict)
    myStr = cookie_reverseParser(myObj)
    return myStr
    
    
def main():

    myCookie = profile_for("michal@yahoo.com")
    encCookie_b64 = ECB_fixed_oracle(myCookie)
    encCookie = encCookie_b64.decode('base64')
    
    decryptCookie = byte_ECB_decryption(ECB_fixed_oracle,encCookie)
    
    print myCookie
    print encCookie
    print decryptCookie

if __name__ == "__main__":
    main()


#print cookieParser("foo=bar&baz=qux&zap=zazzle")
#print profile_for("foo@bar.com")

