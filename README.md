# Unit1_CaseStudy
### 1.Write a program which will find factors of given number and find whether the factor is even or odd. ###
  #### Factors.py ####
### 2.Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically. ###
  #### WordsSorting.py ####
### 3.Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line. ###
  #### FindEvenDigitNumbers.py ####
### 4.Write a program that accepts a sentence and calculate the number of letters and digits. ###
  #### FindNumDigitsLetters.py ####
### 5.Design a code which will find the given number is Palindrome number or not. ###
  #### Palindrome.py ####
  
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Unit2_CaseStudy1
 ###  1.What is the output of the following code? ###
 #### nums =set([1,1,2,3,3,3,4,4]) ####
 #### print(len(nums)) ####
 #### Hint:Set consists unique element ####
  ##### Ans : 4 #####
 ### 2.What will be the output? ###
 #### d ={"john":40, "peter":45} ####
 #### print(list(d.keys())) ####
 #### Hint:d.keys()isthefunctionwhichwillshowkeys. ####
  ##### Ans : ['john', 'peter'] #####
### 3.A website requires a user to input username and password to register. Write a program to check the validity of password given by user. ###
#### Following are the criteria for checking password: ####
-  1. At least 1 letter between [a-z] 
-  2. At least 1 number between [0-9]
-  1. At least 1 letter between [A-Z]
-  3. At least 1 character from [$#@] 
-  4. Minimum length of transaction password: 6
-  5. Maximum length of transaction password: 12
#### Hint: In case of input data being supplied to the question, it should be assumed to be a console input. ####
  ##### Q03.py #####
### 4.Write a for loop that prints all elements of a list and their position in the list. ###
#### a = [4,7,3,2,5,9] 
#### Hint: Use Loop to iterate through list elements.
  ##### Q04.py #####
#### 5.Please write a program which accepts a string from console and print the characters that have even indexes. ####
#### Example: If the following string is given as input to the program:H1e2l3l4o5w6o7r8l9d
#### Then, the output of the program should be:Helloworld
  ##### Q05.py #####
#### 6.Please write a program which accepts a string from console and print it in reverse order.
#### Example: If the following string is given as input to the program: rise to vote sir
#### Then, the output of the program should be:ris etov ot esir
  ##### Q06.py #####
#### 7.Please write a program which count and print the numbers of each character in a string input by console.
#### Example: If the following string is given as input to the program:abcdefgabc
#### Then, the output of the program should be:a,2 c,2 b,2 e,1 d,1 g,1 f,1
  ##### Q07.py #####
#### 8.With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],   write   a program to make a list whose elements are intersection of the above given lists.
  ##### Q08.py #####
#### 9.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
  ##### Q09.py #####
#### 10.By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].
  ##### Q10.py #####
#### 11.By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
  ##### Q11.py #####
#### 12.By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
  ##### Q12.py #####
#### 13.Please  write  a  program  to  randomly  generate  a  list  with  5  numbers,  which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
  ##### Q13.py #####
#### 14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).Example:If the following n is given as input to the program:5Then, the output of the program should be:3.55
  ##### Q14.py #####
  
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Unit2_CaseStudy2
### Case Study II
### Domain –Telecom
### focus –Optimization
### Business challenge/requirement 
### LifeTel  Telecomis the latest entrant in the highly competitive Telecom market of Singapore. It issues SIM to the verified users. Till now verification was manual through the photocopy of approved id card document. However government has recently introduced Social ID called Reference ID which is mapped to fingerprint of user. LifeTel should now verify user against the fingerprint and Reference ID
### Key issues
### Build a system where when user enters Reference ID it is encrypted, so that hackers cannot view the mapping of Reference ID and finger print
### Considerations 
### System should be secure
### Data volume
### -NA
### Additional information-
### NA
### Business benefits
### Company will be able to quickly issue SIM to user and expected gain in volume is approximately 10 times as the manual process of verification is replaced with secure automated system
### Approach to Solve
### You have to use fundamentals of Python taught in module 2
### 1.Read the input from command line –Reference ID
### 2.Check for validity –it should be 12 digits and allows on number and alphabet
### 3.Encrypt the Reference ID and print it for reference
### Enhancements for code
### You can try these enhancements in code
### 1.Allow some special characters in ReferenceID
### 2.Give the option for decryption to user
## EncryptRefID.py ##
