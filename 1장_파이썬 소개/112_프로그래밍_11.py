# 사용자로부터 파일이 위치한 드라이브 이름(C) 디렉토리 이름(\test\), 파일이름(Sample), 확장자(py)를 받아서
# 완전한 파일 이름 (c:\test\sample.py)으로 만드는 프로그램을 작성해보자.

d_name = input("드라이브 이름을 입력하세요 : ")
dir_name = input("디렉토리 경로(\\test\\) : ")
f_name = input("파일 이름을 입력하세요 : ")
ext = input("확장자명 입력 : ")

print(f"완전한 이름은 {d_name}:{dir_name}{f_name}.{ext}")