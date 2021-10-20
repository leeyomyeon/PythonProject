def solution(n, t, m, timetable):
    # 도착 시간을 먼저 분으로 만들고 정렬시킴
    tt = []
    for st in timetable:
        time = st.split(":")
        hour = int(time[0]) * 60
        minute = int(time[1])
        tt.append(hour + minute)

    list.sort(tt)

    # 첫 차의 출발시간은 0900 = 540분
    # t분 간격으로 n대까지 탐색
    idx = 0
    ans = 0
    for arrive in range(540, 540 + t * n, t):
        cnt = 0 # 버스에탄사람
        for i in range(idx, len(tt)):
            if tt[i] <= arrive: # 버스 도착시간보다 적을경우
                cnt += 1
                idx += 1
            if cnt == m:    # 버스에 M명이 다 차면
                break

        if arrive == 540 + t * (n - 1): # 막차
            if cnt < m: # 자리남으면
                ans = arrive
            else:       # 자리꽉찼으면 그전사람한테 붙어서 타면 됨
                ans = tt[idx - 1] - 1
            break

    answer = ''
    if len(str(ans // 60)) == 2:
        answer += str(ans // 60)
    else:
        answer += '0' + str(ans // 60)
    answer += ":"
    if len(str(ans % 60)) == 2:
        answer += str(ans % 60)
    else:
        answer += '0' + str(ans % 60)

    return answer


N = [1, 2, 2, 1, 1, 10]     # 횟수
T = [1, 10, 1, 1, 1, 60]    # 간격(분)
M = [5, 2, 2, 5, 1, 45]     # 최대 승객 수
TT = [["08:00", "08:01", "08:02", "08:03"], ["09:10", "09:09", "08:00"], ["09:00", "09:00", "09:00", "09:00"], ["00:01", "00:01", "00:01", "00:01", "00:01"], ["23:59"], ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]]
# 크루들이 대기열에 도착하는 시간

for i in range(len(N)):
    print(solution(N[i], T[i], M[i], TT[i]))