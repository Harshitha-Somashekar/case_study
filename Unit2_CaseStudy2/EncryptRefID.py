import random

retry = True
while retry:
    retry = False
    referenceID = input("Enter Reference ID:")
    if len(referenceID) != 12:
        print("Reference ID length should be 12 characters. Retry..........!!!")
        retry = True
        continue
    if referenceID.isalnum() == False:
        print("Reference ID includes characters other than digits or letters. Retry..........!!!")
        retry = True
        continue
print("Reference ID accepted!!!")

encryptReferenceIDDict = {}
for i in referenceID:
    encryptReferenceIDKey = random.randint(1000,1255)
    encryptReferenceIDDict.setdefault(i,encryptReferenceIDKey)

encryptReferenceIDStr = ""
for i in referenceID:
    encryptReferenceIDStr += str(encryptReferenceIDDict.get(i))
print(encryptReferenceIDStr)
    
decryptReferenceIDStr = ""
for i in range(0,len(encryptReferenceIDStr),4):
    for key, value in encryptReferenceIDDict.items():
        if(str(value) == encryptReferenceIDStr[i:i+4]):
            decryptReferenceIDStr += str(key)
print(decryptReferenceIDStr)
