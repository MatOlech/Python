# def equals(x: int, y: int) -> None:
#     if x == y:
#         print("Yes")
#     if x != y:
#         print("No")


# def main():
#     x = int(input("First: "))
#     y = int(input("Second: "))
#     equals(1,1)

# main()
def compare(x: int, y: int) -> int:
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1

def main():
    x = int(input(" Team A: ?"))
    y = int(input("Team B: ?"))
    if compare(x,y) == 1:
        print("Team A wins")
    if compare(x,y) == 0:
        print("Draw")
    if compare(x,y) == -1:
        print("Team B wins")

    e1 = int(input(" Employee A ?"))
    e2 = int(input("Employee B ?"))

    if compare(e1,e2) == 1:
        print("Emp A ")
    if compare(e1,e2) == 0:
        print("Emp A == Emp B")
    if compare(e1,e2) == -1:
        print("Emp B")


main()