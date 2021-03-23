def solution(s):
    answer = len(s)
    str_len = int(len(s) / 2)

    for i in range(1, str_len+1):
        result_str = ""
        compare_str = s[:i]
        count = 1

        for j in range(i, len(s), i):
            if compare_str == s[j:j+i]:
                count += 1
            else:
                if count > 1:
                    result_str += str(count)
                result_str += compare_str
                compare_str = s[j:j + i]
                count = 1

        if count > 1:
            result_str += str(count)
        result_str += compare_str

        answer = min(answer, len(result_str))

    return answer


k = ["ababcdcdababcdcd"]
for s in k:
    print(solution(s))