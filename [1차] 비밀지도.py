def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        bin_str = format(arr1[i] | arr2[i], 'b').zfill(n)
        str = ""
        for j in range(n):
            if bin_str[j] == '1':
                str += "#"
            elif bin_str[j] == '0':
                str += " "

        answer.append(str)

    return answer


n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))