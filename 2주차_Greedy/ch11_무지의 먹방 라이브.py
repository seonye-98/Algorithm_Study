'''
이취코테 p316 실전문제: 무지의 먹방 라이브
2019 카카오 신입 공채
'''
import time
start_time = time.time() #측정 시작

#타임오버

def solution(food_times, k):
    answer = 0
    while k > 0:
        if food_times[answer] > 0:
            food_times[answer] -= 1
            k -= 1
        answer += 1
        answer %= len(food_times)
        
    while food_times[answer] == 0:
        answer += 1
        
    if [0]*len(food_times) == food_times:
        answer = -2
    return answer + 1




end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력