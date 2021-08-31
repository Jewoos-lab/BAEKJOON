# 7567

S = input()

# S = input().split()이 아니라
# 반드시 S = list(S)를 통해 각 인덱스를 가질수 있게 해줌
# S = input().split()을 하면 ['((((']이런식으로 인덱스 하나에 다들어감.
S = list(S)

# 생각해보니까 h를 for문안에 넣으면 for문이 시작될때마다 h =10 으로 초기화됨
# 또한 range(len(S))가 아니라 range(1,len(S))임 왜냐면
# 첫번째는 이미 10으로 고정임
h = 10

for i in range(1, len(S)):
       if S[i-1] == S[i]:
              h += 5
       else:
              h += 10

print(h)

