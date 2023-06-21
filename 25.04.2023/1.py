# def main():
#     for _ in range(10):
#         print(str_range(10))


# def str_range(n):
#     l = "a"
#     w = "b"
#     result = []
#     for i in range(n):
#         result.append(l + w)
#         return result



# main()

# def main():
#     n = int(input("Give n"))
#     minus(n)
#     print("meow \n" * n)


# def minus(n):
#     while n < 0:
#         n = int(input("Give positive N"))
#         if n > 0:
#             return n
# main()



# while True:
#     n: int = int(input("What's N?"))
#     if n > 0:
#         break
# for _ in range(n):
#     print("meow")



# def main():
#     get_number()
#     print(trapeze(a, b, h))


# def get_number():
#     while True:
#         a: float = float(input("What's a?"))
#         b: float = float(input("What's b?"))
#         h: float = float(input("What's h?"))
#         if a > 0 and b > 0 and h > 0:
#             break
#         trapeze(a,b,h)

# def trapeze(a, b, h):
#     result = 1 / 2 * (a + b) * h
#     return result

# main()






# def trapeze_field(a, b, h):
#     return 1 / 2 * (a + b) * h

# def get_number(prompt: str) -> float:
#     while True:
#         a: float = float(input(prompt))
#         if a > 0:
#             break

# def main():
#     a : float = get_number("What's a?")
#     b : float = get_number("What's b?")
#     h : float = get_number("What's h?")
#     field = trapeze_field(a, b, h)
#     print(field)

# main()



students = ["Hermione", "Harry", "Ron"]

lenght = len(students)


for i in range(lenght):
    print(students[i])

