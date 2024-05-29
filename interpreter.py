def main ():
    expression = input("Expression:")

    x = int(expression.split()[0])
    y = expression.split()[1]
    z = int(expression.split()[2])

    match y :
        case "+":
            print(sum(x,z))
        case "*":
            print(mult(x,z))
        case "-":
            print(sub(x,z))
        case "/":
            print(div(x,z))

def sum (x,y):
    return float(x + y)

def mult (x,y):
    return float(x * y)

def sub (x,y):
    return float(x - y)

def div (x,y):
    return float(x / y)

main ()