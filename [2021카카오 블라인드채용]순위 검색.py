def solution(info, query):
    answer = []
    for q in query:
        q = q.split(" ")

        count = 0   # 지원자 수
        for infoStr in info:
            infoStr = infoStr.split(" ")
            lang = False
            position = False
            career = False
            food = False
            score = False

            if q[0] == '-' or q[0] == infoStr[0]:
                lang = True

            if q[2] == '-' or q[2] == infoStr[1]:
                position = True

            if q[4] == '-' or q[4] == infoStr[2]:
                career = True

            if q[6] == '-' or q[6] == infoStr[3]:
                food = True

            if int(q[7]) <= int(infoStr[4]):
                score = True

            if lang and position and career and food and score:
                count += 1

        answer.append(count)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))