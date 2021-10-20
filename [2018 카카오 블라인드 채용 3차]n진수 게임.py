T = "0123456789ABCDEF"
def convert(n, base):
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):   # n = 진법, t = 문자열 갯수, m = 플레이어수, p = 차례
    answer = ''
    tmpStr = ''
    num = 0     # 시작숫자
    p -= 1      # 인덱스 계산을 위해 1 감소

    while True:
        if len(tmpStr) >= (t * m):
            break
        # N진수 변환을 해준 값을 임시 문자열에 넣고
        tmpStr += convert(num, n)
        # 다음순서로 넘어가고
        num += 1

    for i in range(p, len(tmpStr), m):
        if len(answer) == t:
            break
        answer += tmpStr[i]

    return answer


N = [2, 16, 16]
T = [4, 16, 16]
M = [2 ,2 , 2]
P = [1, 1, 2]
for i in range(len(N)):
    print(solution(N[i], T[i], M[i], P[i]))

# 0111
# 02468ACE11111111
# 13579BDF01234567