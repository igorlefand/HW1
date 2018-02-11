str = input ("Enter string: ")
cstr = len(str)
str = str.lower()
aCount = str.count("a")
eCount = str.count("e")
iCount = str.count("i")
oCount = str.count("o")
uCount = str.count("u")
print ("Vowel letters in string")
allCount = aCount + eCount + iCount + oCount + uCount
print (allCount)


