# 사용자에게 하나의 문자를 입력받기. 문자가"R"이나 "r"이면 "Rectangle"을 출력.
# "T", "t"이면 Triangle 출력, C/c면 Circle을 출력하는 프로그램. 그 외 문자는 Unknown 출력

text = input("하나의 문자를 입력하세요 : ")

if text == "T" or text == "t":
    print("Triangle")
elif text == "R" or text == "r":
    print("Rectangle")
elif text == "C" or text == "c":
    print("Circle")
else:
    print("Unknown")


# -----------------------------

# text = input("하나의 문자를 입력하세요 : ").lower()

# if text == "t":
#     print("Triangle")
# elif text == "r":
#     print("Rectangle")
# elif text == "c":
#     print("Circle")
# else:
#     print("Unknown")
