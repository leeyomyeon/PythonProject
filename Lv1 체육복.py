def solution(n, lost, reserve):
    n -= len(lost)

    for i in range(len(lost)):
        if lost[i] in reserve:
            t = reserve.index(lost[i])
            reserve[t] = -1
            lost[i] = -1
            n += 1

    for i in range(len(lost)):
        if lost[i] - 1 in reserve:
            t = reserve.index(lost[i] - 1)
            reserve[t] = -1
            n += 1
            continue
        elif lost[i] + 1 in reserve:
            t = reserve.index(lost[i] + 1)
            reserve[t] = -1
            n += 1
            continue

    return n


n = 5
lost = [2,4,5]
reserve = [1,3,5]
print(solution(n, lost, reserve))