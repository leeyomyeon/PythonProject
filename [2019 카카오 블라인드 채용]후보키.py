from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    c_key = []
    for i in range(1, col + 1):
        c_key.extend(combinations(range(col)), i)

    tmp = []
    for key in c_key:
        tmp = [tuple([item[key] for key in key]) for item in relation]
        if len(set(tmp)) == row:
            tmp.append(key)

    answer = set(tmp[:])
    for i in range(len(tmp)):
        for j in range(i + 1, len(tmp)):
            if len(tmp[i]) == len(set(tmp[i]).intersection(set(tmp[j]))):
                answer.discard(tmp[j])

    return len(answer)



relations = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relations))