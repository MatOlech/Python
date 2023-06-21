def convert(time: str) -> float:
    time = time.split(":")
    minutes = float(time[1]) / 60
    return float(time[0]) + minutes

def dish(hours: float) -> str:
    if 7 <= hours <= 8:
        return "breakfast time"
    elif 12 <= hours <= 13:
        return "lunch time"
    elif 18 <= hours <= 19:
        return "dinner time"


def main():
    time = input("What time is it? ")
    hours = convert(time)
    print(dish(hours))

main()