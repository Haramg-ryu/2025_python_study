# 사용자로부터 정수를 받음. 3의 배수면 "Python" 출력, 5의 배수면 "Express" 출력. 3의배수 && 5의 배수면  Python Express 출력

user_num = int(input("정수를 입력하세요 : "))

if user_num % 3 == 0 and user_num % 5 == 0:
    print("Python Express")
elif user_num % 5 == 0:
    print("Express")
elif user_num % 3:
    print("Python")