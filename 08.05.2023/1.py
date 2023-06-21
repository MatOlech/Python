students = [
        {"name": "Harry", "surname": "Potter", "patronus": "Stag", "grades": "},
        {"name": "Hermione", "surname": "Granger", "patronus": "Otter", "grades": marks[]},
        {"name": "Ron", "surname": "Weasly", "patronus": "Jack Russel", "grades": "5"}
    ]

def find_student(name,surname) -> str:

    for i in range(len(students)):
        student = students[i]
        if name == student["name"] and surname == student["surname"]:
            return student


def main():
    name = input("Give name a student")
    surname = input("Give surname a student")
    find_student(name,surname)
    print(find_student(name,surname))


main()
# for student in students:
    # print(student)
        # for i in range(len(students)):
    # student = students[i]
    # print(student["name"])
# Literacja list na 2 różne sposoby
