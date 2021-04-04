def solution(p):
    answer = ''

    if p == '':
        return ''

    check = False

    num = 0
    for i in range(len(p)):
        if p[i] == ')':
            num -= 1
        elif p[i] == '(':
            num += 1

        if abs(num) == 1:    # 짝이 맞지 않을경우(개수 불일치)
            check = True
        if num == 0:
            if check:
                answer += '('
                answer += solution(p[i + 1:len(p) - i -1])
                answer += ')'

                for j in range(1, i):
                    if p[j] == ')':
                        answer += '('
                    else:
                        answer += ')'

                return answer

            else:               # 개수 일치
                answer += p[0 : i + 1]
                answer += solution(p[i + 1:len(p) - i -1])
                return answer


ps = ["(()())()", ")(", "()))((()"]
for p in ps:
    print(solution(p))