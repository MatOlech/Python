def main():
    mark: str = grade(51)
    print(mark)


def grade(score: int) -> str:
    if score > 90:
        return "A"
    elif score > 80:
        return "B"
    elif score > 70:
        return "C"
    elif score > 60:
        return "D"
    elif score > 50:
        return "E"
    else:
        return "F"


def test() -> None:
    if grade(50) != "F":
        print("Test failed = 50")
    if grade(60) != "E":
        print("Test failed = 60")
    if grade(61) != "D":
        print("Test failed = 61")
    if grade(94) != "A":
        print("Test failed")

#main()
test()
