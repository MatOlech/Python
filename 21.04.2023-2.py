def main():
age = 12

def age_range(age: int) -> str:
    if 0 <= age <= 9:
        return "child"
    elif 10 <= age <= 18:
        return "teen"
    elif 19 <= age <= 60:
        return "adult"
    elif age => 60:
        return "old"


def test() -> None:
    # age: int = 16
    # range = age_range(age)
    if age_range(16) != "teen":
        print("Test failed")
    # if age_range() != teen:
        # print("Test failed")

insurance("toyota, 23000") ---> ma wydrukować kwotę do zapłąty


