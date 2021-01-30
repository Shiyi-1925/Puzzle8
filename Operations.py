n = 9
# 1   2   3
# 4   5   6
# 7   8   0
target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
# 0   1   2
# 3   4   5
# 6   7   8
possible_moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4, 6], [
    1, 3, 5, 7], [2, 4, 8], [3, 7], [4, 6, 8], [5, 7]]


def isOK(board):
    return sorted(board) == [0, 1, 2, 3, 4, 5, 6, 7, 8]


def isReachable(board):
    newBoard = board.copy()
    newBoard[board.index(0)] = 9
    cnt = 0
    for i in range(n):
        for j in range(i):
            if newBoard[j] > newBoard[i]:
                cnt += 1
    return cnt % 2 == 0

def DistHamming(board):
    cpt = 0

    for i in range(n):
        if board[i] != target[i]:
            cpt += 1
    return cpt


def DistManhattan(board):
    dist = 0

    for i in range(n):
        if board[i] == 0:
            dist += abs(2-i//3)+abs(2-i % 3)
        else:
            distRow = abs(i//3-(board[i]-1)//3)
            distCol = abs(i % 3-(board[i]-1) % 3)
            dist += distRow+distCol
            # print(distRow, distCol)
    return dist


def isGoal(board):
    return board == target

# list of new boardsGroup with possible movements


def moves(board):
    boardsGroup = []
    ind = board.index(0)
    cells = possible_moves[ind]
    for pos in cells:
        boardsGroup.append(swap(board, ind, pos))
    return boardsGroup


def swap(board, i, j):
    newBoard = board.copy()
    newBoard[i] = board[j]
    newBoard[j] = board[i]
    return newBoard


if __name__ == "__main__":
    # # unit test for input check
    # print(isOK([2, 6, 8, 0, 1, 3, 5, 4, 7]))

    # # unit test for distance calculation
    # testM = [8, 1, 4, 7, 5, 6, 2, 0, 3]
    # print("Test case:", testM)
    # print("Hamming distance:", DistHamming(testM))
    # print("Manhattan distance:", DistManhattan(testM))

    # # unit test for moves
    # testM = [8, 4, 5, 7, 0, 6, 2, 1, 3]
    # print(moves(testM))

    # # unit test for reverse pair
    # testM = [8, 1, 4, 7, 5, 6, 2, 0, 3]
    # print(testM, "is reachable?", isReachable(testM))

    # unit test for reverse pair
    testM = [2, 1, 3, 4, 8, 5, 7, 6, 0]
    print(testM, "is reachable?", isReachable(testM))
