
# def snake_case(camel):
#     snake = ""
#     for i in camel:
#         if i.isupper():
#             snake += f"_{i.lower()}"
#         else: 
#             snake += i

#     return snake

        


# def main():
#     camel = input("Camel Case: ").strip()
#     print("snake_case:",snake_case(camel))

# main()

# def coke_machine(valid_coins: list) -> None:
#     amount = 50
#     print(amount)
#     while amount > 0:
#         coin = int(input("Insert coin: "))
#         if coin in valid_coins:
#             amount -= coin
#             print("Change owned: ",amount)
#         else:
#             print("Amount due: ",amount)


        

# def main():
#     valid_coins = [5, 10, 25]
#     # coke_machine(valid_coins)
#     amount = 50
#     print(amount)
#     while amount > 0:main()
#         coin = int(input("Insert coin: "))
#         if coin in valid_coins:
#             amount -= coin
#             print("Change owned: ",amount)
#         else:
#             print("Amount due: ",amount)

    
    




# vowels = ["a", "e", "i", "o","u"]

# def without_vowels(text):
#     new_text = ""
#     for letter in text:
#         if letter.lower() not in vowels:
#             new_text += letter

#     return new_text
    
# def main():
#     text = input("Input: ").strip()
#     print(f"Output: {without_vowels(text)}")

# main()


fruit_to_calories = {"apple": 130, "avocado": 50}

def find_calories(fruit:str) -> int:
    return fruit_to_calories[fruit]


def main():
    print(find_calories("applee"))

# def is_valid(plate: str) -> bool:
#     if not check_two_letters(plate):
#         return False
#     if not 2 <= len(plate) <= 6:
#         return False
#     if not plate.isalnum():
#         return False
#     if not plate[0:1].isalpha():
#         return False
    
#     if check_two_letters(plate) and check_length(plate) and check_special_characters(plate) and valid_position(plate):
#         return True
#     return False

# def check_two_letters(plate: str) -> bool:
#     if len(plate) >= 2:
#         return plate[0:2].isalpha()
#     return False

# def check_length(plate: str) -> bool:
#     return 2 <= len(plate) <= 6

# def valid_position(plate: str) -> bool:
#     return plate[0:1].isalpha()

# def check_special_characters(plate: str) -> bool:
#     return plate.isalnum()

# def main():
#     plate = input("Enter a plate: ")

#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

main()

