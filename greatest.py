a=int (input("enter first num: "))
b=int(input("enter second num: "))
c=int(input("enter third num: "))
if a>b and a>c:
    print("a is greatest")
elif b>c and b>a:
    print("b is greatest")
else:
    print("c is greatest")        