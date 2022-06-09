num=int(input("enter"))
onum=num
rem=0
n=0
len=len(str(num))
i=0
while (i<len):
    rem=num%10
    n=n*10+rem
    num=num//10
    i=i+1
if onum==n:
    print("num is palin")
else:
    print("num is not palin")