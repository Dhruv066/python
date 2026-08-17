a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
c=int(input("enter the third number: "))
if a>b:
    if a>c:
        print(a,"is the maximum number")
        if b>c:
            print(b ,"is the middle number")
            print(c,"is the minimum number")
        else:
            print(c ,"is the middle number")
            print(b,"is the minimum number")
if b>a:
    if b>c:
        print(b,"is the maximum number")
        if a>c:
            print(a ,"is the middle number")
            print(c,"is the minimum number")
        else:
            print(c ,"is the middle number")
            print(a,"is the minimum number")
else :
    print(c,"is the maximum number")
    if a>b:
        print(a ,"is the middle number")
        print(b,"is the minimum number")
    else:
        print(b ,"is the middle number")
        print(a,"is the minimum number")