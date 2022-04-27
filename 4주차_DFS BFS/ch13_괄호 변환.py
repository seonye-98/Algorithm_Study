def bracketDivide(p):
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            return p[:left+right], p[left+right:]

# 문제 3번 과정
def checkBracket(u):
    left, right = 0, 0
    if u[0] == ')' or u[-1] == '(':
        return False
    else:
        return True

# 문제 4번 과정
def reverseBracket(u):
    bracket = ''
    for i in range(len(u)):
        if u[i] == '(':
            bracket += ')'
        else:
            bracket += '('
    return bracket

def solution(p):
    answer = ''
    while len(p) != 0:
        u, v = bracketDivide(p)
        if checkBracket(u):
            answer += u
            p = v
        else:
            answer += '(' + solution(v) + ')' + reverseBracket(u[1:-1])
            break

    return answer



'''
오답
def check(p):
    arr = []
    for word in p:
        if word == '(':
            arr.append(word)
        else:
            if len(arr) > 0:
                arr.pop()
            else:
                return False
    if len(arr) == 0:
        return True

def divide(arr, _p):
    u = ''
    v = ''
    for idx in range(len(_p)):
        u = _p[:idx+1]
        v = _p[idx+1:]
        if check(u) and not check(v):
            arr.append(u)
            divide(arr, v)
            break
        elif not check(u) and check(v):
            arr.append(u)
            arr.append(v)
            break
            
def backward(p):
    tmp = ""
    for w in p:
        if w == "(":
            tmp += ")"
        else:
            tmp += "("
    return tmp
        
    
    
def solution(p):
    answer = ''

    if p == '':
        return answer
    else:
        if check(p):
            answer = p
            print('first check', check(p))
            return answer
        else:
            div_arr = []
            divide(div_arr, p)
            print('div_arr', div_arr)
            tmp = "("
            tmp1 = ""
            tmp2 = ""
            idx = 0
            for _ in range(len(div_arr)-1):
                if not check(div_arr[idx+_]) and check(div_arr[idx+_+1]):
                    tmp1 = div_arr[idx+_]
                    tmp2 = div_arr[idx+_+1]
                    idx = idx+_
                    break
            print("hi",tmp1, tmp2)
            tmp += (tmp2+")")
            print(tmp)
            if not check(tmp1[1:len(tmp1)-1]):
                tmp += backward(tmp1[1:len(tmp1)-1])
            else:
                tmp += tmp1[1:len(tmp1)-1]
            print(tmp)
            return ''.join(div_arr[:idx])+tmp
                
                
    return answer
'''