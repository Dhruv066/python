time=input("enter the time in format(HH:MM:SS AM/PM)")
if time[-2:]=="AM" and time[:2]=="12":
    print("00"+time[2:8])
elif time[-2:]=="AM":
    print(time[0:8])
elif time[-2:]=="PM" and time[:2]=="12":
    print(time[0:8])
else:
    print(str(int(time[:2])+12)+time[2:8])
