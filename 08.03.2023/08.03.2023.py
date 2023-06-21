# print(input("Name?"), input("surname?"), input("age?"), sep = "\n")
# def register(name, surname, position = "dev", level="junior", salary="2400"):
#     print("Registered:" + surname, name, level, position, salary, sep="|")

# register("Mateusz", "Olech")
# register("Mateusz", "Olech", level="senior", position="developer", salary="3400")
# register("Mateusz", "Olech", position="Developer", level=input("level: "), salary=input("salary: "))
# register("Mateusz", "Olech", position="developer")




# name = input("What's your name")
# surname = input("What's your surname")
# age = input("Age: ")
# separator = input("separator: ")
# print(name, surname, age, sep=separator)
name = input("What's your name: ")
surname = input("What's your surname: ")
fullname = f"{surname}, {name}"
print(fullname)
