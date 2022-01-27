# 1931번

meeting_time = []
for i in range(int(input())):
    start_time, end_time = map(int, input().split())
    meeting_time.append((start_time, end_time))

meeting_time = sorted(meeting_time, key = lambda x:(x[1], x[0]))
cnt = 0  # 회의 개수를 저장할 변수
before_end_time = 0  # 회의의 마지막 시간을 저장할 변수

for i, j in meeting_time:
    if i >= before_end_time:
        cnt += 1
        before_end_time = j
print(cnt)
