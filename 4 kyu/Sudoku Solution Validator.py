def validSolution(board):
    reverse = [[] for i in range(9)]
    cubes = [[] for i in range(9)]
    for i in range(9):
        for j in range(9):
            reverse[i].append(board[j][i])
            if i <= 2:
                cubes[j//3].append(board[i][j])
            elif 2 < i <= 5:
                cubes[(j+9)//3].append(board[i][j])
            else:
                cubes[(j+18)//3].append(board[i][j])
    for i in range(9):
        if sum(board[i]) | sum(reverse[i]) | sum(cubes[i]) != 45:
            return False
    return True

print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                                  [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                  [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                  [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                  [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                  [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                  [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                  [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                  [3, 0, 0, 4, 8, 1, 1, 7, 9]]))

##
# def validSolution(board):
#     blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
#     return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)