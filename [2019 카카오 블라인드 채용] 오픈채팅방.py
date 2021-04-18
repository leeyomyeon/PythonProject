def solution(record):
    answer = []
    # 명령어 / uid / 닉네임

    inout = []
    dic = {}
    for i in range(len(record)):
        record[i] = record[i].split(" ")
        if record[i][0] == "Change":
            continue
        inout.append([record[i][1], record[i][0]])  # UID0000 / 입장, 퇴장

    for i in range(len(record)):
        if record[i][1] not in dic:
            dic[record[i][1]] = record[i][2]
        elif record[i][0] == "Enter" and record[i][1] in dic:
            dic[record[i][1]] = record[i][2]
        if record[i][0] == "Change":
            dic[record[i][1]] = record[i][2]

    for i in range(len(inout)):
        str = ""
        if inout[i][1] == "Enter":
            str = "님이 들어왔습니다."
        elif inout[i][1] == "Leave":
            str = "님이 나갔습니다."

        answer.append(dic[inout[i][0]] + str)

    return answer


records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(records))