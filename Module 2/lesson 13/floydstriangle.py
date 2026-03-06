#Write a program to demonstrate a Floyd triangle pattern?#floyds triangle
#1
#2 3
#4 5 6
n=int(input("Enter number of rows "))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num ,end=" ") # part of inner loop
        num=num+1
    print() # part of outer loop
 

