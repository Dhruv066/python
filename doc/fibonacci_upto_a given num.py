# program to print fibonacci upto nth term

n=int(input("enter the number upto which fibonicci series you want"))
a,b=0,1
for i in range(1,n+1):
    print(a)
    a,b=b,a+b