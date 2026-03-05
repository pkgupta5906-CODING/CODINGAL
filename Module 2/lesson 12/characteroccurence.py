# Write a program to check how many times a character is repeated in a word?
word=input("Enter any word  : ")
char=input("Enter any character :")
if len(char)==1:
    i=0
    count=0
    while (i<len(word)):
        if (word[i])==char:
            count+=1
        else:
             pass # to do nothing 
        i=i+1
    print("The caharcter ",char, " occurs ",count,"times in the word ",word )
else:
    print("Enter a single character")
         

    
