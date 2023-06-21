def bank(greet: str) -> int:
    greet = greet.lower().lstrip()
    # if greet starts with Hello.
    if greet.startswith("hello "):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100

def main():
    greet = input("Greetings:")
    print(bank(greet) + "$")

main()