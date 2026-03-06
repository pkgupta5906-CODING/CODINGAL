# Write a program to demonstrate a right angle triangle pattern?# similar to half pyramid pattren of stars
n=int(input("Enter the number of rows")) 
for i in range(n):
    for j in range(i+1):
        print("* ",end=" ")
    print()
