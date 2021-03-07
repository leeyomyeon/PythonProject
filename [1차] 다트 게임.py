def solution(dartResult):
    score = []
    dartResult = dartResult.replace('10', 'X')

    for k in dartResult:
        if k >= '0' and k <= '9' or k == 'X':   # 0 ~ 10 사이의 숫자일 때
            if k == 'X':
                score.append(10)
            else:
                score.append(int(k))

        elif k == 'S' or k == 'D' or k == 'T':
            l = len(score)
            if k == 'D':
                score[l - 1] = score[l - 1] * score[l - 1]
            elif k == 'T':
                score[l - 1] = score[l - 1] * score[l - 1] * score[l - 1]

        elif k == '*' or k == '#':
            l = len(score)
            if l >= 2 and k == '*':
                score[l - 2] *= 2
                score[l - 1] *= 2
            elif l == 1 and k == '*':
                score[l - 1] *= 2
            elif k == '#':
                score[l - 1] *= -1

    answer = 0

    for i in score:
        answer += i

    return answer


dartResult = ['1S2D*3T', '1D2S#10S', '1D2S0T', '1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
for k in dartResult:
    print(solution(k))