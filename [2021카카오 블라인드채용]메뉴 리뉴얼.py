# from itertools import combinations
# from collections import Counter
#
# def solution(orders, courses):
#     answer = []
#     for course in courses:
#         tmp = []
#         for order in orders:
#             combination = combinations(sorted(order), course)
#             tmp += combination
#         counter = Counter(tmp)
#         if len(counter) != 0 and max(counter.values()) != 1:
#             answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
#
#     return sorted(answer)

# 내장함수 안쓰고 해보기

def combination(cnt, start, order, course):
    if cnt == course:
        tmp_list = list
        print(list)
        list.clear()
        return tmp_list

    for i in range(start, len(order)):
        list.append(order[i])
        combination(cnt+1, i+1, order, course)

def solution(orders, courses):
    answer = []
    for course in courses:
        global list
        tmp = []
        for order in orders:
            list = []
            list = combination(0, 0, sorted(order), course)




# orders = [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], ["XYZ", "XWY", "WXA"]]
# course = [[2, 3, 4], [2, 3, 5], [2, 3, 4]]
orders = [["XYZ", "XWY", "WXA"]]
course = [[2,3,4]]
for i in range(len(orders)):
    print(solution(orders[i], course[i]))
