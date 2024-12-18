def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b


n1= int(input("Enter a number: " ))
n2= int(input("Enter a number: "))

op = input("Choose an operator [+, -, x, /]: ")

if op == "+":
    res = add(n1,n2)
    print(f"The sum of {n1} and {n2} is {res}")
    
elif op == "-":
    res = sub(n1,n2)
    print(f"The difference of {n1} and {n2} is {res}")
    
elif op == "x":
    res = mul(n1,n2)
    print(f"The product of {n1} and {n2} is {res}")
    
elif op == "/":
    res = div(n1,n2)
    print(f"The quotient of {n1} and {n2} is {res}")