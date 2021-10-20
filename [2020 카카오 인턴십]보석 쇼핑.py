def solution(gems):
    # 시작 끝 인덱스
    start = 0
    end = 0
    # 젬 종류 수
    gem_num = len(set(gems))
    # 배열 길이
    gems_len = len(gems)
    answer = [0, gems_len]
    # 중복 배제를 위한 딕셔너리 생성 및 초기화
    dict = {}

    while True:
        if end >= gems_len: # 끝 인덱스가 배열 길이 넘어가면 종료
            break
        if gems[end] not in dict:   # 현재 보석이 딕셔너리에 없으면 새로 추가
            dict[gems[end]] = 1
        else:                       # 현재 보석이 딕셔너리에 있으면 개수 늘림
            dict[gems[end]] += 1
        end += 1            # 그리고 끝 인덱스 늘림

        if len(dict) == gem_num: # 0번 인덱스부터 마지막으로 담았을때의 보석의 종류가 전체 보석의 종류와 같아지면
            while start < end:  # 시작 위치를 앞당겨본다
                if dict[gems[start]] <= 1: # 보석이 1개 이하로 있으면 그냥 끝
                    break
                dict[gems[start]] -= 1 # 2개 이상이면 한칸 당겨도 됨
                start += 1

            if abs(start - end) < abs(answer[1] - answer[0] + 1): # 구간 길이가 적으면 answer의 최소값을 다시 지정해줌
                answer = [start + 1, end]

    return answer


G = [["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
     ["AA", "AB", "AC", "AA", "AC"],
     ["XYZ", "XYZ", "XYZ"],
     ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]
for g in G:
    print(solution(g))