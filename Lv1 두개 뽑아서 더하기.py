def solution(numbers):
    answer = []

    for i in range(len(numbers) - 1):
        for j in range (i+1, len(numbers)):
            sum = 0
            sum += numbers[i] + numbers[j]
            answer.append(sum)

    answer = list(set(answer))
    answer.sort()
    return answer

a = [5, 0, 2, 7]

print(solution(a))