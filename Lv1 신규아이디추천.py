def solution(new_id):

    id1 = ""
    for str in new_id.lower():
        if (str >= "a" and str <= "z") or (str >= '0' and str <= '9') or str == "-" or str == "_" or str == ".":
            id1 += str
        else:
            continue

    id2 = id1[0]

    for i in range(1, len(id1)):
        if id1[i - 1] == '.' and id1[i] == '.':
            continue
        else:
            id2 += id1[i]

    if id2[0] == '.':
        id2 = id2[1:]
    if len(id2) >= 1 and id2[len(id2) - 1] == '.':
        id2 = id2[:len(id2) - 1]

    if len(id2) == 0:
        id2 += "a"

    if len(id2) >= 16:
        id2 = id2[:15]

    if id2[len(id2) - 1] == '.':
        id2 = id2[:len(id2) - 1]

    if len(id2) <= 2:
        while(1):
            if len(id2) == 3:
                break
            id2 += id2[len(id2) - 1]

    return id2

new_id = "123_.def"
print(solution(new_id))