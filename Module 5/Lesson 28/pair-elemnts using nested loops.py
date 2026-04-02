class pair_elemants:
    def sum(self,nums,sum):
         

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==sum:
                    return i,j

value=int(input("enter a sum : "))
obj=pair_elemants()
result=obj.sum((10,20,30,40,50,60,70),value)
if result:
    print("index 1 is equal to",result[0],"index 2 is equal to ",result[1])
else:
    print("No pair found !!")