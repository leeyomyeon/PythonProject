def solution(answers):
    a, b, c = 0, 0, 0
    a_count, b_count, c_count = 0, 0, 0
    aAnswer = [1,2,3,4,5]
    bAnswer = [2,1,2,3,2,4,2,5]
    cAnswer = [3,3,1,1,2,2,4,4,5,5]

    for i in answers:
        if i == aAnswer[a]:
            a_count += 1

        if i == bAnswer[b]:
            b_count += 1

        if i == cAnswer[c]:
            c_count += 1

        a += 1
        b += 1
        c += 1
        if a == len(aAnswer):
            a %= len(aAnswer)
        if b == len(bAnswer):
            b %= len(bAnswer)
        if c == len(cAnswer):
            c %= len(cAnswer)

    answer = []
    if a_count >= max(b_count, c_count):
        answer.append(1)
    if b_count >= max(a_count, c_count):
        answer.append(2)
    if c_count >= max(a_count, b_count):
        answer.append(3)

    return answer

answers = [1,2,3,4,5]
print(solution(answers))
answers = [1,3,2,4,2]
print(solution(answers))
