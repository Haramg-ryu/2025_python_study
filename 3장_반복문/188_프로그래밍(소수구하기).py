# 50개의 소수 구하기
# 1과자신만이 가지는 수

# 찾아야 하는 소수 개수

N_PRIMES = 50
number = 2   # 시작 숫자를 2부터 시작
count = 0

while count < N_PRIMES:
    divisor = 2  # 나누는 수를 2부터 시작하자. number과 다름!!
    prime = True

    while divisor < number:   # divisor 나누려는 수 / number 소수인지 검사할 숫자
        if number % divisor == 0:  # num이 7이면 2~6으로 divisor로 나눔
            prime = False  # 소수가 아니라면
            break          # 빠져나온다.
        divisor += 1   # 나누려는 수를 1 더한다. (7이었으면 2~6, 8이면 2~7)
    if prime:          # 만약 True라면 = 즉 소수라면
        count += 1     # 찾은 개수를 1개 증가시킨다.
        print(number, end=" ")  # 그 소수를 화면에 출력한다.