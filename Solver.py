import time
import Operations as ops

priorities = ["Hamming", "Manhattan"]


class Node:
    board = None
    step = 0
    value = -1
    parent = None
    priority = None

    def __init__(self, inputBoard, step, parent, priority):
        self.board = inputBoard
        self.step = step
        if priority == "Hamming":
            self.value = ops.DistHamming(inputBoard) + self.step
        else:
            self.value = ops.DistManhattan(inputBoard) + self.step
        self.parent = parent
        self.priority = priority


def puzzleSolver(initBoard):
    startTime = time.time()
    if(not ops.isOK(initBoard)):
        raise Exception("Input invalid")

    # check if reachable
    if(not ops.isReachable(initBoard)):
        endTime = time.time()
        output = {}
        output["reachable"] = False
        output["iterations"] = 0
        output["duration"] = endTime-startTime
        output["priority"] = None
        output["nb_moves"] = 0
        return output

    outputs = []
    for i in range(len(priorities)):
        result, nodeList = AStar(initBoard, priorities[i])
        if result != None:
            outputs.append(result)
    outputs.sort(key=lambda x: (x["nb_moves"], x["iterations"], x["duration"]))
    return outputs[0]


def AStar(initBoard, priority):
    startTime = time.time()
    output = {}
    visited = []
    openList = [Node(initBoard, 0, None, priority)]
    count = 0

    while(openList):
        if openList == []:
            return None
        # check if finish
        currentNode = openList[0]
        visited.append(currentNode.board)
        # print(currentNode.board)
        if(ops.isGoal(currentNode.board)):
            endTime = time.time()
            output["reachable"] = True
            output["iterations"] = count
            output["duration"] = endTime-startTime
            output["priority"] = priority
            output["nb_moves"] = openList[0].step
            return output, openList

        openList.pop(0)
        count += 1
        nextMoves = ops.moves(currentNode.board)
        for nextMove in nextMoves:
            if nextMove not in visited:
                openList.append(
                    Node(nextMove, currentNode.step+1, currentNode, priority))
        openList.sort(key=lambda x: x.value)


if __name__ == "__main__":
    # testBoard = [8, 3, 5, 1, 2, 7, 4, 6, 0]
    testBoard = [2, 1, 3, 4, 8, 5, 7, 6, 0]
    print(puzzleSolver(testBoard))
