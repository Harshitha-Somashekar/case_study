string = input("Enter a string:")
stringDict = {}
for i in string:
    stringDict.setdefault(i,string.count(i))
    
#sorts the dictionary based on value. PS: got from google :-)
for i in sorted(stringDict.items(),key=lambda x: x[1], reverse=True):
    print(i)
