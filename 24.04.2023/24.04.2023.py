def main():
    n = 4
    print(f(n))


def f(n: int) -> int:
    return 0 if n % 2 == 0 else 1
    # albo
    # return n % 2 == 0

def find_house(name: str) -> str:
    match name.capitalize():
        case "Harry" | "Hermione":
            return "Gryffindor"
        case "Draco":
            return "Slytherin"
        case _:
            return "Who?"
    # if name == "Harry":
    #     return "Gryffindor"
    # elif name == "Draco":
    #     return "Slytherinn"

def test():
    if find_house("harry") != "Gryffindor":
        print("Test Failed")
    if find_house("Draco") != "Slytherin":
        print("Test Failed")

# main()
test()






# Nazwa Lista Argumentów i typ zwracany