# def build_rectrangle(height: int, width: int) -> str:
    # brick = ""
    # for i in range(height):
        # for i in range(width):
            # brick += "#"
        # brick += "\n"
# 
# 
    # return brick
# 
# def test(height,width,expection):
    # if expection == build_rectrangle(height,width):
        # print("Test passed")
    # else:
        # print("Test not passed")
# 
# 
# def main():
    # test(5, 5, "#####\n#####\n#####\n#####\n#####\n\n")
# 
# 
# main()
# 
# def get_int(prompt) -> int:
#     while True:
#         try:
#             x = int(input(prompt))
#             # x = int(x)
#             return x
#         except ValueError:
#             print("x is not intinger")



# def main():
#     prompt = input("What is your prompt?")
#     # x = input("What's x?")
#     print(get_int(prompt))
    


# main()




def fibonnacci(n: int) -> int:
    elements = [0, 1]
    for i in range(n):
        result = elements[n-1] + elements[n-2]
        return result


def main():
    n = int(input("What's N?"))
    print(fibonnacci(n))

main()