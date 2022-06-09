num=int(input("enter the number"))
i=0
sum=0
while i<=num:
    a=int(input("enter the second number"))
    sum=sum+a
    i=i+1
total_sum=sum
average=total_sum//num
print(average) 
if average%5==0:
    print("average it is multiple by 5")
else:
    print("average is not multiple by 5")