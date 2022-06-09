a=int(input("enter the number"))
i=2
while i<=a//2:
  if a%i==0:
    print("it is not a print number")
    break
  i=i+1
else:
  print("it is a print number")