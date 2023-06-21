# def square(x:int) -> int:
#     return x * x

# x = (int(input("Podaj liczbę która ma być podniesiona do kwadratu: ")))
# print(square(x))


# def add(x,y):
#     z = x + y
#     return z

# def multiply(x, y, z):
#     return  x * y * z


# def main():
#     x = int(input("First number: "))
#     y = int(input("Second numer: "))
#     z = add(x,y)
#     print(multiply(z, z, z))

# main()
def change(first: str, second:str ,third:str) -> str:
    # first.capitalize()
    # second.lower()
    #third
    return f"{first.capitalize()} {second.lower()} {third.lower()}."


def main():
    # first = input("First word:")
    # second = input("Second word:")
    # third = input("Third word:")
    print(change("TEST", "test", "TEST"))

main()
