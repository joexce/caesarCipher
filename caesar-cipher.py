import sys

dbString = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chiperText = ""
decryptText = ""
index= 0
x = 0

def encypt(strInput,shifting,dbString,chiperText,index,x):
    for plainChar in strInput:
        if plainChar == " ":
            chiperText += " "
        for dbChar in dbString:
            if plainChar == dbChar:
                x = (index + shifting) % 26
                chiperText += dbString[x]
            index += 1
    print chiperText
def decrypt(strInput,shifting,dbString,decryptText,index,x):
    for chiperChar in strInput:
        if chiperChar == " ":
            decryptText += " "
        for dbChar in dbString:
            if chiperChar == dbChar:
                x = (index - shifting) % 26
                decryptText += dbString[x]
            index += 1
    print decryptText

methodInput = str(sys.argv[1])
strInput = str(sys.argv[2])
shifting = str(sys.argv[3])

if(methodInput == "-c"):
    encypt(strInput, int(shifting), dbString,chiperText,index,x)

if(methodInput == "-d"):
    decrypt(strInput, int(shifting),dbString,decryptText,index,x)
