def solution(s):
    answer = []
    s = s.replace("{", "")
    s = s.split("},")
    for i in range(len(s)):
        if s[i].find("}") >= 0:
            s[i] = s[i].replace("}", "")
        s[i] = s[i].split(",")
    # 문자열 전처리 후 리스트로 변환

    s.sort(key=lambda x:len(x))
    # 길이순으로 정렬됨

    for si in s:
        for sj in si:
            if int(sj) not in answer:
                answer.append(int(sj))

    return answer




sA = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}", "{{20,111},{111}}", "{{123}}", "{{4,2,3},{3},{2,3,4,1},{2,3}}"]
for si in sA:
    print(solution(si))