dbString = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
plainText = "apa yang kamu dengar adalah untuk anda sendiri"
chiperText = ""
decryptText = ""
index= 0
x = 0

for plainChar in plainText:
    if plainChar == " ":
        chiperText += " "
    for dbChar in dbString:
        if plainChar == dbChar:
            x = (index + 23) % 26
            chiperText += dbString[x]
        index += 1
print chiperText

for chiperChar in chiperText:
    if chiperChar == " ":
        decryptText += " "
    for dbChar in dbString:
        if chiperChar == dbChar:
            x = (index - 23) % 26
            decryptText += dbString[x]
        index += 1
print decryptText
