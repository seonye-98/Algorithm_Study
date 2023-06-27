import itertools

n = int(input())
num_arr = list(map(int, input().split()))
#plus, minus, mult, div
cal_arr = list(map(int, input().split()))
cal_char_arr = []
for _ in range(4):
    tmp = []
    if cal_arr[_] > 0:
        if _ == 0:
            tmp = '+ ' * cal_arr[_]
            cal_char_arr.extend(tmp.split())
        elif _ == 1:
            tmp = '- ' * cal_arr[_]
            cal_char_arr.extend(tmp.split())
        elif _ == 2:
            tmp = '* ' * cal_arr[_]
            cal_char_arr.extend(tmp.split())
        elif _ == 3:
            tmp = '/ ' * cal_arr[_]
            cal_char_arr.extend(tmp.split())


alllist = list(set(itertools.permutations(cal_char_arr, n-1)))
ans = []
for c_arr in alllist:
    result = num_arr[0]
    idx = 0
    for num in num_arr[1:]:
        if c_arr[idx] == '+':
            result += num
        elif c_arr[idx] == '-':
            result -= num
        elif c_arr[idx] == '*':
            result *= num
        elif c_arr[idx] == '/':
            result = int(result/num)
        idx += 1
    ans.append(result)
    #print(c_arr, result, _min, _max)
ans.sort()
print(ans[-1])
print(ans[0])
            

#print(num_arr, cal_arr, cal_char_arr)