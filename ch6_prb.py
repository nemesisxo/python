a1=int(input("enter first:"))
a2=int(input("enter second:"))
a3=int(input("enter third:"))
a4=int(input("enter fourth:"))
if a1>a2 and a1>a3 and a1>a4:
    print("first is largest")
elif a2>a1 and a2>a3 and a2>a4:
    print("second is largest")
elif a3>a1 and a3>a2 and a3>a4:
    print("third is largest")
else:
    print("fourth is largest")