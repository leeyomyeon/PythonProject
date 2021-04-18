import re
import copy

def solution(expression):
    answer = 0

    operator = []
    for s in expression:
        if s == '*' or s == '-' or s == '+':
            operator.append(s)
    # "100-200*300-500+20"
    operand = re.split("[\+\-\*]", expression)
    # 100 200 300 500 20
    #  -   *   -  +
    # +, -, * 순으로 순서 정함
    # 012, 021, 102, 120, 201, 210
    oper = ['+', '-', '*']
    priority = [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]

    for pr in priority:
        tmp_operator = copy.deepcopy(operator)
        tmp_operand = copy.deepcopy(operand)

        for p in pr:
            while True:
                if oper[p] not in tmp_operator:
                    break
                else:
                    i = tmp_operator.index(oper[p])
                    if tmp_operator[i] == oper[p]:
                        tmp_operator.remove(oper[p])
                        res = 0
                        if oper[p] == '+':
                            res = int(tmp_operand[i]) + int(tmp_operand[i + 1])
                        elif oper[p] == '-':
                            res = int(tmp_operand[i]) - int(tmp_operand[i + 1])
                        elif oper[p] == '*':
                            res = int(tmp_operand[i]) * int(tmp_operand[i + 1])

                        del tmp_operand[i + 1]
                        del tmp_operand[i]

                        tmp_operand.insert(i, res)

        if abs(tmp_operand[0]) > answer:
            answer = abs(tmp_operand[0])

    return answer


expressions = ["100-200*300-500+20", "50*6-3*2"]
for e in expressions:
    print(solution(e))