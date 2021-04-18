def solution(m, n, board):
    answer = 0

    board_arr = []
    for b in board:
        board_arr.append(list(b))

    while True:
        isok = True
        # 사라질 블록 위치 저장할 배열
        visited = [[0 for p in range(n)]for q in range(m)]

        # 0,0 부터 m-1, n-1 까지 2 by 2 탐색
        for i in range(m - 1):
            for j in range(n - 1):
                if board_arr[i][j] != "" and (board_arr[i][j] == board_arr[i + 1][j] == board_arr[i][j + 1] == board_arr[i + 1][j + 1]):
                    isok = False
                    visited[i][j] = visited[i + 1][j] = visited[i][j + 1] = visited[i + 1][j + 1] = 1
                    continue

        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    # 사라진 블록 개수 세기
                    answer += visited[i][j]
                    # 현재 위치가 사라질 블록 위치이므로 공백으로 변환
                    board_arr[i][j] = ""

        # 빈 공간으로 위의 블럭 내려와야 함
        # 맨 아래 칸 부터 확인함,
        for i in range(m-1, -1, -1):
            for j in range(n):
                while board_arr[i][j] == "":
                    con = False

                    for k in range(i, -1, -1):
                        if board_arr[k][j] != "":
                            con = True

                    for k in range(i, -1, -1):
                        if k == 0:
                            board_arr[k][j] = ""
                        else:
                            board_arr[k][j] = board_arr[k - 1][j]

                    if not con:
                        break

        if isok:
            break

    return answer


m = [4, 6]
n = [5, 6]
board = [["CCBDE", "AAADE", "AAABF", "CCBBF"], ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]]
for i in range(2):
    print(solution(m[i], n[i], board[i]))