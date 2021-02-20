def solution(participant, completion):
    participant.sort()
    completion.sort()
    completion.append(" ")
    answer = ''

    for i in range(len(completion)):
        if completion[i] == participant[i]:
            continue
        else :
            answer = participant[i]
            break

    return answer

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["marina", "josipa", "nikola", "filipa"]

print(solution(participant, completion))