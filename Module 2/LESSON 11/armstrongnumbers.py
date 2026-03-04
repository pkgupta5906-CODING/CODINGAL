# Write a program to check if the number entered by the user is an Armstrong number or not?
n=int(input("Enter any number : "))
sum=0 # initialisation
temp=n
while temp>0:
     digit=temp%10 # %10(remainder when divided by 10.) gives the last digit.
     sum+=digit**3 
     temp//=10 # //10(floor division ) removes the last digit.

if n==sum : 
     print(n,"is an armstrong number")
else:
     print(n,"is not an armstrong number .")