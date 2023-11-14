word = input("input number or word:")
myChar = []
for i in range(len(word)):
    myChar.append(str(word)[i:i+1])
#print(myChar)
myChar2 = []
for i in range(len(word)-1,-1,-1):
    myChar2.append(str(word)[i:i+1])
#print(myChar2)
if myChar == myChar2:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
