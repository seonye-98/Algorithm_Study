'''
이취코테 p96 실전문제: 숫자 카드 게임
'''
import time
start_time = time.time() #측정 시작

def solution(n, build_frame):
    def init(n):
        res = []
        for i in range(n + 1):
            temp = []
            for j in range(n + 1):
                temp.append([j, i, 0, 0])
            res.append(temp)
        return res

    def check(now_block, x, y):
        res = True
        if now_block[y][x][2] == 1:  # 기둥
            if y == 0 or now_block[y - 1][x][2] == 1 or now_block[y][x][3] == 1 or (
                    x > 0 and now_block[y][x - 1][3] == 1):
                res = True
            else:
                return False
        if now_block[y][x][3] == 1:  # 보
            if (y > 0 and now_block[y - 1][x][2] == 1) or (y > 0 and x < n and now_block[y - 1][x + 1][2] == 1) \
                    or (x > 0 and x < n and now_block[y][x - 1][3] == 1 and now_block[y][x + 1][3] == 1):
                res = True
            else:
                return False
        return res

    block = init(n)
    # build_frame: (가로, 세로, 종류, 설치여부)
    for k in range(len(build_frame)):
        build = build_frame[k]
        x, y = build[0], build[1]
        typ, act = build[2], build[3]
        if act == 1:
            if typ == 0:  # 기둥
                block[y][x][2] = block[y][x][2] + 1
                if check(block, x, y) is False:
                    block[y][x][2] = block[y][x][2] - 1
            else:  # 보
                block[y][x][3] = block[y][x][3] + 1
                if check(block, x, y) is False:
                    block[y][x][3] = block[y][x][3] - 1
        else:  # act == 0
            if typ == 0:  # 기둥
                if block[y][x][2] > 0:
                    block[y][x][2] = block[y][x][2] - 1
                    if (check(block, x, y) and check(block, x, y + 1) and check(block, x - 1, y + 1)) is False:
                        block[y][x][2] = block[y][x][2] + 1
            else:  # 보
                if block[y][x][3] > 0:
                    block[y][x][3] = block[y][x][3] - 1
                    if (check(block, x, y) and check(block, x - 1, y) and check(block, x + 1, y)) is False:
                        block[y][x][3] = block[y][x][3] + 1

    #     return block
    # answer: (가로, 세로, 종류)
    answer = []
    for i in range(len(block)):
        for j in range(len(block)):
            if block[j][i][2] > 0:
                answer.append([block[j][i][0], block[j][i][1], block[j][i][2] - 1])
            if block[j][i][3] > 0:
                answer.append([block[j][i][0], block[j][i][1], block[j][i][3]])
    return answer

#출처: https://ai-information.blogspot.com/2019/12/2020-kakao-blind-recruitment.html

# def check_build_col(answer_array, build):
#     #기둥위에 기둥
#     #print('check_build_col',answer_array, build)
#     if [build[0], build[1]-1, 0] in answer_array:
#         return True
#     elif [build[0]-1, build[1], 1] in answer_array:
#         return True
#     return False

# def check_build_bar(answer_array, build):
#     #answer : 설치된 곳
#     #build : 보 설치할 곳
#     #print('check_build_bar',answer_array, build)
#     for answer in answer_array:
#         if answer[2] == 0 and answer[1] == 0:
#             if answer[0] == build[0] and answer[1]+1 == build[1]:
#                 return True
#             elif answer[0] -1 == build[0] and answer[1]+1 == build[1]:
#                 return True
#         elif answer[2] == 0 and answer[1] > 0:
#             if answer[0] == build[0]+1 and answer[1] == build[1]:
#                 return True
#             elif answer[0] == build[0] and answer[1] == build[1]:
#                 return True
#             elif answer[0] == build[0] and answer[1]+1 == build[1]:
#                 return True
#             elif answer[0]-1== build[0] and answer[1]+1 == build[1]:
#                 return True
    
#     left_bar = [build[0]-1, build[1], 1]
#     right_bar = [build[0]+1, build[1], 1]
#     if left_bar in answer_array and right_bar in answer_array:
#         return True
#     return False
            
# def solution(n, build_frame):
#     answer = []
#     for build in build_frame:
#         if build[3] == 1:
#             #설치
#             if 0<= build[0] <= n and 0<= build[1] <=n:
#             #격자 범위 만족
#                 if build[2] == 0:
#                     #기둥 설치
#                     if build[1] == 0:
#                         #바닥에 붙어있는 경우
#                         answer.append(build[:3])
#                         #print(sorted(answer))
#                     else:
#                         if check_build_col(answer, build):
#                             answer.append(build[:3])
#                             #print(sorted(answer))
#                 else:
#                     #보 설치
#                     if build[2] != 0:
#                         #바닥에 안붙어 있는 경우 보 설치가능
#                         if check_build_bar(answer, build):
#                             answer.append(build[:3])
#                             #print(sorted(answer))
#             else:
#             #격자 범위 불만족
#                 pass
#         elif build[3] == 0:
#             #삭제
#             if build[2] == 0:
#                 #기둥삭제
#                 if [build[0]-1, build[1]+1,1] in answer and [build[0], build[1]+1,1] in answer:
#                     answer.remove(build[:3])
                
        
#         answer.sort()
#     return answer

end_time = time.time()
print(f"{end_time - start_time:.5f} sec")#수행 시간 출력