import math
def Add(a,b):
    return (int(a)+ int(b))
def Subtract(a,b):
    return (int(a)-int(b))
def Multiply(a,b):
    return (int(a)*int(b))
def Divide(a,b):
    return (int(a)/int(b))
def SquareRoot(a):
    return(math.sqrt(int(a)))
def Square(a,b):
    return(math.pow(int(a),int(b)))

run = True

while run:
    Equation = input("What equation do you want to do? (add/subtract/multiply/divide/square root/square): ")
    if Equation.lower() == "add": 
        x = Add(input("Enter Number 1: ") , input("Enter Number 2: "))
        print(x)
    elif Equation.lower() == "subtract":
        x = Subtract(input("Enter Number 1: ") , input("Enter Number 2: "))
        print(x)
    elif Equation.lower() == "multiply":
        x = Multiply(input("Enter Number 1: ") , input("Enter Number 2: "))
        print(x)
    elif Equation.lower() == "divide":
        x = Divide(input("Enter Number 1: ") , input("Enter Number 2: "))
        print(x)
    elif Equation.lower() == "square root":
        x = SquareRoot(input("Enter Your Number: "))
        print(x)
    elif Equation.lower() == "square":
        x = Square(input("Enter the number you want to exponent: "),(input("Enter the power: ")))
        print(x)
    elif Equation.lower() == "stop":
        run = False
    else:
        print("This is not a registered operator")