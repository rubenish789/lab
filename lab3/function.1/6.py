def reversed(str):
    words = str.split()
    words.reverse()
    strRev = ""
    for word in words:
        strRev = strRev + word + " "
    print (strRev)

str = input()
reversed(str)