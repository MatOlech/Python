def dodawanie(a,b):
    c = a + b
    return c

def odejmowanie(a,b):
    c = a - b
    return c

def mnozenie(a,b):
    c = a * b
    return c

def dzielenie(a,b):
    c = a / b
    return c

# a = float(input("Podaj a"))
# b = float(input("Podaj b"))
while True:
    try:
        a = float(input("Podaj liczbę: "))
        break
    except ValueError:
        print("Nieprawidłowe dane. Podaj jedną liczbę.")

while True:
    try:
        b = float(input("Podaj liczbę: "))
        break
    except ValueError:
        print("Nieprawidłowe dane. Podaj liczbę.")

while True:
    c = input("Podaj działanie (+ lub /): ")
    if c == '+' or c == '/' or c == '*' or c == '/':
        break
    else:
        print("Nieprawidłowe dane. Podaj + lub /.")

if c == '+':
    print(dodawanie(a,b))
elif c == '-':
    print(odejmowanie(a,b))
elif c == '*':
    print(mnozenie(a,b))
elif c == '/':
    print(dzielenie(a,b))