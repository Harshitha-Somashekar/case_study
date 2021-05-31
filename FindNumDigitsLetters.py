sentence = input("Enter the sentence:")
numOfDigits = 0
numOfLetters = 0
for i in sentence:
    if i.isdigit():
        numOfDigits += 1
    elif i.isalpha():
        numOfLetters += 1
print("Sentence : " + sentence)
print("\t Number of Digits  : " + str(numOfDigits))
print("\t Number of Letters : " + str(numOfLetters))
