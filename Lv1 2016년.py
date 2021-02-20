def solution(a, b):
    ans = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    result = 0
    for i in range(a):
        result += month[i]
    result += b

    answer = ans[result % 7]
    return answer


a = 5
b = 24
print(solution(5, 24))
