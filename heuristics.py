import math


def ManhattenHeuristic(state):
    goal = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]
    sum = 0
    for i in range(0, 3):
        for j in range(0, 3):
            tile = state.value[i][j]
            if tile == 0:
                continue
            for m in range(0, 3):
                for n in range(0, 3):
                    if tile == goal[m][n]:
                        sum += abs(i - m) + abs(j - n)
    return sum


def EuclidHeuristic(state):
    goal = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]]
    sum = 0
    for i in range(0, 3):
        for j in range(0, 3):
            tile = state.value[i][j]
            if tile == 0:
                continue
            for m in range(0, 3):
                for n in range(0, 3):
                    if tile == goal[m][n]:
                        sum += math.sqrt(math.pow(i - m, 2) +
                                         math.pow(j - n, 2))
    return sum
