n=int(input("enter"))
i=2
s=0
sp=1
sm=0
while i<=n:
    if i%2==0:
        sp=sp+i**2
    else:
        sm=sm+i**2
    i=i+1
    s=sp-sm
print(s,end=" ")

