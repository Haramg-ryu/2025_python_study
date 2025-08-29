# 두 리스트로 식당에서 식사하는 사람의 모든 조합을 출력해보자.

persons = ["Kim", "Park", "Lee", "Choi"]
restaurants = ["Korean", "American", "French", "Chinese"]
cities = ["Seoul", "Busan", "Daejeon"]

for person in persons:
    for restaurant in restaurants:
        for city in cities:
            print(person + "이 " + city + "지역의 " + restaurant + " 식당을 방문")