#a, b = map(int, input().split)

_list = [1,2,3,4,5]

# 가변인자 *(asterisk)
print(*_list)
print(type(_list))

# Unpacking
a = _list
print(a)

#List Comprehension
## 백준 온라인 저지 1920번 "수 찾기" (<http://boj.kr/1920>)
# import sys
# input = sys.stdin.readline

# _ = input()
# _set = set(map(int, input().split()))
# q = input()
# _list = list(map(int, input().split()))

# print(*[1 if dt in _set else 0 for dt in _list], sep = '\\n')

test_list = ['Test', 'test', 'TEST', 'tteesstt']
converted_list = list(set(map(lambda string: string.lower(), test_list))) # test, tteesstt

square = [[x ** 2 for x in range(3)] for _ in range(3)]
print(square) # [[1, 4, 9], [1, 4, 9], [1, 4, 9]]

fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(_dict.setdefault('strawberry', 0)) # 0

from collections import defaultdict

movie_review = [('Train to Busan', 4), ('Clementine', 5), ('Parasite', 4.5), ('Train to Busan', 4.2), ('Train to Busan', 4.5), ('Clementine', 5)]

index = defaultdict(list)

for review in movie_review:
    index[review[0]].append(review[1]) 
    # {'Train to Busan': [4, 4.2, 4.5], 'Clementine': [5, 5], 'Parasite': [4.5]}

print(*index.keys())
print(*index.values())
print(*index.items())

string = 'I am Hungry...'
print(string[6:0:-1]) # -1 : 역순으로
print(string[0:7:3]) # index: 0 - 6
print("".join(reversed(string))) #2

import itertools
_list = [1, 2, 3, 4]
iter = itertools.combinations(_list, 2) # 조합 : 12 13 14 23 24 34

iter = itertools.permutations(_list, 2) # 순열 : 12 13 14 21 23 24 31 32 34 41 42 43

iter = itertools.combinations_with_replacement(_list, 2) # 중복조합 : 11 12 13 14 22 23 24 33 34 44

iter = itertools.product(_list, repeat=2) # Cartesian Product : 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44

_list = [1, 2, 3, 4, 5]
print(sum(_list))

_list2 = [1, 2, 3, 4, 5, 6, 7, 8]

print(", ".join(map(str,_list2))) 
#join은 정수형 리스트에서 사용할 수 없어, 문자열 리스트로 변형 후 join할 수 있다.

_list3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for idx, val in enumerate(_list3):
    print(idx, val)


from collections import Counter
print(Counter('hello world').most_common()) 
# [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter('hello world').most_common(2) # [('l', 3), ('o', 2)]

def rotate(arr):
    return list(zip(*arr[::-1]))

_arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(*_arr[::-1])
print(rotate(_arr))
# [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

