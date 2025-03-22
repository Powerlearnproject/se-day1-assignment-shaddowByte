

while True:
    num1 = int(input("enter the first number: "))
    num2 = int(input("enter the second number: "))
    symbol = input("enter the symbol for operation(* - + /): ")
    
    if symbol == "+":
        ans = num1 + num2
        print(f"{num1} + {num2} = {ans}")
        break
    elif symbol == "-":
        ans = num1 - num2
        print(f"{num1} - {num2} = {ans}")
        break
    elif symbol == "*":
        ans = num1 * num2
        print(f"{num1} * {num2} = {ans}")
        break
    elif symbol == "/":
        if num2 == 0:
            print("division by zero error")
        else :
            ans = num1 /num2
            print(f"{num1} + {num2} = {ans}")
            break
    else:
        print("invalid symbol input")


