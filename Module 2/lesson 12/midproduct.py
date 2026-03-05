# Write a program to calculate the product of the middle digits of a number?
n=int(input("Enter any number of 4 or more digits : "))
t=n
numlen=0
while t>0:
    numlen=numlen+1
    t=int(t/10)
if numlen>=4:
    numlen=int(numlen/2)
    check=0
    while n>0:
        rem=n%10
        if check==numlen:
            mid1=rem
        elif check==numlen-1:
            mid2=rem
        n=int(n/10)
        check=check+1
    prod=mid1*mid2
    print("The produt of middigits is ",prod)
else:
    print("Its not 4 or more than 4 digit number")
    
    
        
        