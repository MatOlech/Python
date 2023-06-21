def deep():
    deeping = input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip()
    answers = ["42", "forty two", "forty-two"]
    if deeping in answers:
        print("Yes")
    else:
        print("No")

def main():
    deep()

main()