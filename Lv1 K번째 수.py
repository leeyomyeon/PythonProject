def solution(array, commands):
    answer = []

    for arr in commands:
        i = arr[0] - 1
        j = arr[1]
        k = arr[2] - 1

        tmp_arr = array[i:j]
        tmp_arr.sort()
        answer.append(tmp_arr[k])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
