#method 1 . equation method
base = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = base ** power

print("Result =", result)

#method 2...using for loop
result=1
for i in range(power):
    result=result*base
print("The result is ",result)
