import re
import math

def solution(str1, str2):
    #문자열 전처리
    str1 = str1.lower()
    str2 = str2.lower()

    union = []      # 합집합
    intersection = []   # 교집합

    str1_multi_set = []
    str2_multi_set = []

    # 다중집합 만들기
    for i in range(len(str1) - 1):
        if bool(re.search("[^a-z]", str1[i : i + 2])):
            continue
        str1_multi_set.append(str1[i : i + 2])

    for i in range(len(str2) - 1):
        if bool(re.search("[^a-z]", str2[i : i + 2])):
            continue
        str2_multi_set.append(str2[i : i + 2])

    # 합집합 및 교집합 만들기
    # 집합 만들기 전에 값이 있는지 없는지 확인할 set 생성
    compare_set = set(str1_multi_set + str2_multi_set)
    for s in compare_set:
        i = max(str1_multi_set.count(s), str2_multi_set.count(s))   # 합집합 만들때 사용할 max값
        j = min(str1_multi_set.count(s), str2_multi_set.count(s))   # 교집합 만들때 사용할 max값
        for p in range(i):
            union.append(s)
        for q in range(j):
            intersection.append(s)

    if len(intersection) == 0 and len(union) == 0:
        res = 1
    else:
        res = len(intersection) / len(union)
    answer = math.trunc(res * 65536)
    return answer


str1 = ["FRANCE", "handshake", "aa1+aa2", "E=M*C^2"]
str2 = ["french", "shake hands", "AAAA12", "e=m*c^2"]

for i in range(len(str1)):
    print(solution(str1[i], str2[i]))
