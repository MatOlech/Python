# x = float(input("What's x?"))
# y = float(input("What's y?"))
# znak = (input("Jaki znak? + * / -"))
# if znak == '+':
#     z = x + y
#     print(z)
# elif znak == '-':
#     z = x - y
#     print(z)
# elif znak == '/':
#     z = x / y
#     print(z)
# else:
#     z = x * y
#     print(z)
# def hello():
#     x = input("What's your name?")
#     print(x)

# def hello1():
#     x = 1
#     return x

# def hello2():
#     name = input("What's your name? ")
#     return name
#     print(name)

# hello()
# hello1()
# hello2()

name = input("What's your name?")
surname = input("What's your surname?")

def hello(name,surname):
    return "Hello, " + name + surname


print(hello(name,surname))