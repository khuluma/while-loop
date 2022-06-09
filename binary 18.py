binary=int(input("enter"))
i=1
dec=0
while binary!=0:
    reminder=binary%10
    binary=binary//10
    dec=dec+reminder*i
    i=i*2
print("decimal number is",dec)