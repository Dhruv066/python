day = int(input("enter the number"))
match day:
    case 1 | 2|3|4|5|6|7:
        print ("valid number")
    case _ :
        print("unvalid")
