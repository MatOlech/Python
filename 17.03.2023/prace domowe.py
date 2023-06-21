# def lowercase(small: str)-> str:
#     return f"{small.lower()}"


# def main():
#     small = input("Give text")
#     print(lowercase(small))


# main()

# def strip(givetext):
#     striping = givetext.split()
#     return strip
# def main():
#     givetext = input("Give Text: ")
#     strip(givetext)
#     for i in range(len(givetext)):
#         if (givetext[i] == " "):
#             print("...")
# main()

import re
x = input("")
def better_version(input):
    if not input:
        return "Empty"
    result = re.sub(" ","...",input)
    return result
print(better_version(x))



# def einstein(m):
#     c = int(300000000)
#     e = m*c ** 2
#     return e
# def main():
#     m = int(input("Give m: "))
#     print(einstein(m))

# main()
