'''
이취코테 p323 실전문제: 문자열 압축
'''
import time
start_time = time.time() #측정 시작

import re

def solution(s):
    if len(s) <= 2:
        return len(s)
    resultCount = []
    for i in range(1, len(s)//2 + 1):
        reList = re.sub('(\w{%i})' %i, '\g<1> ', s).split()
        count = 1
        result = []
        for j in range(len(reList)):
            if j < len(reList)-1 and reList[j] == reList[j+1]:
                count += 1
            else:
                if count == 1:
                    result.append(reList[j])
                else:
                    result.append(str(count) + reList[j])
                    count = 1

        resultCount.append(len(''.join(result)))
    
    return min(resultCount)

'''
88점
from collections import Counter

def solution(s):
    answer = len(s)
    
    split_num = len(s)//2
    
    for i in range(1, split_num + 1):
        d_list = []
        ten_up = 0
        for j in range(len(s) // i):
            #print(s[i*j: i*(j+1)],s[i*(j+1): i*(j+2)])
            if s[i*j: i*(j+1)] == s[i*(j+1): i*(j+2)]:
                d_list.append(s[i*j: i*(j+1)])
                #print(dict(Counter(d_list)))
        key_len = len(list(dict(Counter(d_list)).keys()))
        value_sum = sum(list(dict(Counter(d_list)).values()))
        #print(sum(list(dict(Counter(d_list)).values())), len(list(dict(Counter(d_list)).keys())), '//i :',i)
        for _n in list(dict(Counter(d_list)).values()):
            if 10 <= _n+1 < 100:
                ten_up += 1
            elif 100 <= _n+1 < 1000:
                ten_up += 2
            elif _n+1 == 1000:
                ten_up += 3
        answer = min(answer, len(s)-value_sum*i + key_len + ten_up)
        #print(answer, len(s)-value_sum*i + key_len)
    return answer
'''

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력


