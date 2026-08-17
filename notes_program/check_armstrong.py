n=int(input("enter a number"))
t=n
sum=0
l=len(str(n))
while t!=0:
    sum+=((t%10)**l)
    t//=10
if sum==n:  
    print("armstrong")  
else:  
    print("not armstrong")
