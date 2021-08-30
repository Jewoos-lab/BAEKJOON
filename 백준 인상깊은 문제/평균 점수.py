# 11653번

# 이문제는 쉬웠으나, 마지막 출력이 정수형이냐 실수형이냐
# 문제에서 원하는 답은 정수형이라 //를 사용 (5로 나눠떨어지기 때문에
# /를 쓰나 //를 쓰나 결과값은 똑같지만 실수로나오냐 정수로 나오냐의 차이
# ★잘 숙지할것★

sum = 0

for i in range(5):
    score = int(input())
    if score < 40:
        score = 40
    sum += score

print(sum // 5)

# 다른풀이
# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# E = int(input())
#
# sum =0
#
# list = [A,B,C,D,E]
#
# for i in list:
#     if i < 40:
#         i = 40
#     sum += i
# print(sum//5)