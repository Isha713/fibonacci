n=int(input("enter any number"))
a,b=0,1
while n>0:
    print(a,end=" ")
    a,b=b,a+b,
    n-=1