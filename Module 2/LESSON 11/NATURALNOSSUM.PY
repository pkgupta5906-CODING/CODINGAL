#Write a program to find the sum of natural numbers
n=int(input("Enter last number : "))
sum=0 # initialsitaion
i=1
while i <=n: # loop will run from 1 to n
    sum=sum+i
    i=i+1
print("The sum is ",sum)
