# Write a program to demonstrate the numbers in a diamond pattern?
#  1   upper half
# 123  uper half 
#  1   lower half

#   1  upper half
#  123  upper half
# 12345  upper half
#  123   lower half
#   1    lower half
rowsize=int(input("Enter the number of rows"))
if rowsize%2==0: # condition to chcek whentehr rowsize is odd or even
    halfDiamRow=int(rowsize/2)
else:
    halfDiamRow=int(rowsize/2)+1
space=halfDiamRow-1 # number of spaces

# for upper half
for i in range(1,halfDiamRow+1): #  Major for loop --purpose is to get number of rows  
    for j in range(1,space+1):   # Inner for loop 1 -- purpoe to get spaces n column
        print(end=" ")
    space=space-1
    num=1

    for k in range(2*i-1):       # Inner for loop 2----to gte digits and numbers
        print(end=str(num))
        num=num+1
    print()

 # lower half
space=1 # because first row of lower diamond will have 1 space before the numbers.
for i in range(1,halfDiamRow): # Main for loop
    for j in range(1,space+1): # Innner for loop 1- to get space
        print(end=" ")
    space=space+1  
    num=1

    for k in range(1,2*(halfDiamRow-i)): # inner for loop2
        print(end=str(num))
        num=num+1
    print()
    


     