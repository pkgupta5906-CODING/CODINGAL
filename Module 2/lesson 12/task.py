#nested for loop
# for i in range(1,5):
#     for j in range(1,11):
#         print(j,end=' ')
#     print("line 5")
i=1
while i<=5:
    j=1
    while j<=10:
        print(j,end=' ')
        j=j+1
    print('outer loop')
    i=i+1
    
  