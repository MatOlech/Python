# students = ["Hermione", "Harry", "Ron", "Draco"]
# houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
# numbers = [1, 3, 5, 7]
# b = 0
# lenght = len(numbers)
# for i in range(lenght - 1):
#     a = numbers[i] + numbers[i + 1]
#     print(a)

student_to_house = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Draco": "Slytherin"
}

# print(student_to_house["Hermione"])
for student in student_to_house:
    print(f"{student}, "Lives in", {student_to_house[student]}")
