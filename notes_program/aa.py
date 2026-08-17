n=int(input("enter the starting value"))
end=int(input("enter the endi"))
sum1=sum2=0
while n!= end+1:
    if n%2==0:
        sum1+=n
    else :
        sum2+=n
    n+=1

print("sum of even=",sum1)
print("sum of odd=",sum2)
