# Write a program to print all the prime numbers which come in the range entered by the user?
lower=int(input("Enter a lower range : "))

upper=int(input("Enter an upper range : "))
print("Prime numbers between lower an upper limit are ")
for i in range(lower,upper+1):
    if i>1:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
