n=input("enter y string")
a="aeiouAEIOU"
count1=count2=0
for i in n:
    if i in a:
        count1+=1
    else:
        count2+=1
print("vowel",count1)
print("consonent",count2)

