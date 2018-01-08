def string_to_hexString(inputString):
    finalString = ""
    for character in inputString:
        temp = "{0:x}".format(ord(character))
        if ( len(temp) == 1):
            temp = "0" + temp
        finalString += temp
    return finalString