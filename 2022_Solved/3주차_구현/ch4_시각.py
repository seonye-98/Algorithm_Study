'''
이취코테 p113 예제문제: 시각
'''
import time
start_time = time.time() #측정 시작

# N = int(input())

# start = [0,0,0,0,0,0]

# hour_1 = int(N // 10)
# hour_2 = int(N % 10)

# end = [hour_1, hour_2, 5, 9, 5, 9]

# answer = 0

# while start != end:

#   if start[4] != 5 and start[5] == 9:
#     start[5] = 0
#     start[4] += 1
#   elif start[2] == 5 and start[3] == 9 and start[4] == 5 and start[5] == 9:
#     start[2] = 0
#     start[3] = 0
#     start[4] = 0
#     start[5] = 0
#     start[1] += 1
#   elif start[4] == 5 and start[5] == 9:
#     start[4] = 0
#     start[5] = 0
#     start[3] += 1
#   elif start[2] != 5 and start[3] == 9:
#     start[3] = 0
#     start[2] += 1
#   elif start[2] == 5 and start[3] == 9 and start[4] == 5 and start[5] == 9:
#     start[2] = 0
#     start[3] = 0
#     start[4] = 0
#     start[5] = 0
#     start[1] += 1
#   elif start[1] == 9:
#     start[1] = 0
#     start[0] += 1
#   else:   
#     start[5] += 1

#   if 3 in start:
#     answer += 1

# print(answer)

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력