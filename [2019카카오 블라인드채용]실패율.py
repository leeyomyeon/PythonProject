def solution(N, stages):
    user_num = len(stages)

    stage_fail_rate = {}

    for i in range(1, N + 1):
        if user_num == 0:
            stage_fail_rate[i] = 0
            continue
        fail_count = stages.count(i)   # 실패한 사람
        fail_rate = fail_count / user_num
        stage_fail_rate[i] = fail_rate
        user_num -= fail_count          # 성공한 사람(남은사람)

    return sorted(stage_fail_rate, key=lambda x: stage_fail_rate[x], reverse=True)


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))