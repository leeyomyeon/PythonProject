def solution(board, moves):
    answer = 0
    basket = []
    for i in moves:
        index = i - 1

        for j in range (len(board[index])):
            if board[j][index] == 0:
                continue
            else:
                basket.append(board[j][index])
                board[j][index] = 0

            if len(basket) <= 1:
                break
            else:
                k = len(basket) - 1
                if basket[k - 1] == basket[k]:
                    basket.pop(k)
                    basket.pop(k - 1)
                    answer += 2
                break

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))