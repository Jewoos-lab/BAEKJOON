# 5355번

# 첫째 줄에 테스트 케이스의 개수 T
T = int(input())

# T만큼 반복한다.
for i in range(T):
    # 화성 수학식 한 줄을 입력하고 split()을 사용해 리스트 변수로 만든다.
    mars_math = input().split()

    # 인덱스0은 계산을 시작할 값이므로 따로 변수로 만든다.
    num = float(mars_math[0])
    # 인덱스1부터 끝까지는 연산자로써 따로 변수로 만든다.
    operations = mars_math[1:]

    for operation in operations:
        if operation == '@':
            num *= 3
        elif operation == '%':
            num += 5
        else:
            num -= 7
        print(format(num, ".2f"))