
list = [7, 4, 2]

def min(list) -> int:
    min_value = list[0]
    for i in range(len(list) - 1):
        current_value = list[i + 1]
        if current_value < min_value:
            min_value = current_value
    return min_value


print(min(list))

        