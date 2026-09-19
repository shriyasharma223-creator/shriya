a= float(input("enter 1 num: "))
operator=input("enter operator (+,-,*,/,%): ")
b=float(input("enter 2 num: "))
match operator:
    case "+":
        print(a+b)
    case "-":
        print(a-b)    
    case "*":
        print(a*b)
    case "/":
        print(a/b)
    case "%":
        print(a%b)    

    case _:
        print("invalid operator")