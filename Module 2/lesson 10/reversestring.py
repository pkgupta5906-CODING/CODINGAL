#Write a program to reverse the string entered by the user.
str=input("Enter a string : ")
str2=("") 
for i in str :
     str2=i+str2
     #str=hut 
     # ,in iteration 1:i="h" so str2= "h"+""="H"
    #  in iteration 2: i="u" so str2="u"+"h"="uh"
    # in iteration 3, i="t" so str2="t"+"uh"="tuh"

    # str2=str2+i
print("Original string is : ",str)
print("Reversed string is : ",str2)
