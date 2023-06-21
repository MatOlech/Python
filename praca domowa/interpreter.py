def main():
    x, y, z = input("Expression: ").split()
    print(math_interpreter(x, y, z))

def math_interpreter(x,y,z):
    x = float(x)
    z = float(z)
    if y == "+":
        return f"{x+z}"
    elif y == "-":
        return f"{x-y}"
    elif y == "*":
        return f"{x*y}"
    else:
        return f"{x/y}"

main()