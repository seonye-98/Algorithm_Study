'''
이취코테 p96 실전문제: 숫자 카드 게임
'''
import time
start_time = time.time() #측정 시작


import math
import itertools
def solution(n, weak, dist):
    answer = 0
    
    weakSize = len(weak)
    weak = weak + [w+n for w in weak]
    minCnt = math.inf
    for start in range(weakSize):
        for d in itertools.permutations(dist,len(dist)):
            cnt = 1
            pos = start
            for i in range(1,weakSize):
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt-1]:
                    pos = nextPos
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                minCnt = min(minCnt, cnt)
    
    if minCnt == math.inf:
        return -1
    
    return minCnt
'''
def solution(n, weak, dist):
    answer = 0
    
    _list = [0 for _ in range(n)]
    
    for w in weak:
        _list[w] = 1
    dist = sorted(dist, reverse=True)

    student = 0
    idx = 0
    while 1 in _list:
        d = dist[idx]
        #print('distance',d)
        _max = 0
        tmp = []
        tmp2 = []
        for w in weak:
            if w + d + 1 < n:
                tmp.append(_list[w:w+d+1].count(1))
                tmp2.append([dt for dt in  weak if w<= dt <w+d+1])
            else:
                tmp.append(_list[w:].count(1) + _list[:d-n+w+1].count(1))
                tmp2.append([dt if dt < d-n+w+1 or w <= dt else 0 for dt in  weak ])
        #print('tmp',tmp)
        #print('tmp2',tmp2)
        _max = max(tmp)
        min_d = []
        min_d_idx = 0
        if tmp.count(_max)>1:
            idx=0
            for t in tmp2:
                if 0 not in t:
                    min_d.append(t[-1] - t[0])
                else:
                    min_d.append(t[0]+n+1-t[-1])
            #print(min_d)
            _min = min(min_d)
            for d in dist:
                if _min <= d:
                    min_d_idx = d
                    break
            _weak = weak[min_d.index(_min)]
            if _weak + min_d_idx + 1 < n:
                _list[_weak:_weak+min_d_idx+1] = [0 for _ in range(min_d_idx+1)]
            else:
                _list[_weak:] = [0 for _ in range(n-_weak)]
                _list[:min_d_idx-n+_weak+1] = [0 for _ in range(min_d_idx-n+_weak+1)]
            dist.remove(min_d_idx)
            student += 1
            continue
            #print(_list)
        else:
            _weak = weak[tmp.index(_max)]
            if _weak + d + 1 < n:
                _list[_weak:_weak+d+1] = [0 for _ in range(d+1)]
            else:
                _list[_weak:] = [0 for _ in range(n-_weak)]
                _list[:d-n+_weak+1] = [0 for _ in range(d-n+_weak+1)]
            dist.remove(d)
            student += 1
            #print(_list)
        idx += 1
        #print(student)
    return student
'''

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력