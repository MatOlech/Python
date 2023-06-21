# def main():
#     x = "Toyota"
#     y = 1500001
#     print(brand(mark)+mileage(course))


# def brand(mark: str ) -> int:
#     if mark == "Toyota":
#         return 500
#     elif mark == "BMW":
#         return 1000
#     elif mark == "Porsche":
#         return 1500
#     elif mark == "Peugeot":
#         return 2000


# def mileage(course: str) -> int:
#    if 0 <= course <= 50000:
#         return 300
#    elif 50000 <= course <= 100000:
#         return 600
#    elif 100001 <= course <= 150000:
#         return 900
#    elif course >= 150001:
#         return 1200

# def test():
#     if brand("Toyota") + mileage(150001) != 1700:
#         print("Test Failed")
#     if brand("BMW") + mileage(300) != 1300:
#         print("Test Failed")


# # main()
# test()
students = [
        {"name": "Harry", "surname": "Potter"},
        {"name": "Hermione", "surname": "Granger"},
        {"name": "Ron", "surname": "Weasly"}
    ]

def add_new_student(name,surname) -> list:
    new_student = {"name": name, "surname": surname}
    students.append(new_student)
    return students

def main():
    while True:
        command = input(">")
        if command == "add":
            name = input("Name: ").capitalize()
            surname = input("Surname :").capitalize()
            add_new_student(name,surname)
        elif command == "list":
            print(students)
        elif command == "exit":
            break
        else:
            print("Unknown command")
            
            
            
        

main()
