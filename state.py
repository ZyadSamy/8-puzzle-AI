import math
from copy import deepcopy


class State:
    def __init__(self, val, preAction, preState, emptyIndex):
        self.value = val
        self.previousAction = preAction
        self.previousState = preState
        self.emptyIndex = emptyIndex
        self.depth = 0;
        self.cost = 0;

    def __str__(self):
        line = f'-------\n'
        out = ""
        out += line
        for r in self.value:
            out += f'|{r[0]}|{r[1]}|{r[1]}|\n'
            out += line
        return out

    def __gt__(self, state):
        return self.cost > state.cost
        

    def neighbors(self) :
        (row,col) = self.emptyIndex
        actions = []
        neighbors = []

        if (col > 0):
            actions.append("LEFT")
        if (col < 2):
            actions.append("RIGHT")
        if (row > 0):
            actions.append("UP")
        if (row < 2):
            actions.append("DOWN")

        for action in actions:
            neighbors.append(applyAction(self, action, row, col))

        return neighbors

    def ManhattenHeuristic(self):
        goal = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]
        sum = 0
        for i in range(0, 3):
            for j in range(0, 3):
                tile = self.value[i][j]
                for m in range(0, 3):
                    for n in range(0, 3):
                        if tile == goal[m][n]:
                            sum += abs(i - m) + abs(j + n)
        return sum

    def EuclidHeuristic(self):
        goal = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8]]
        sum = 0
        for i in range(0, 3):
            for j in range(0, 3):
                tile = self.value[i][j]
                for m in range(0, 3):
                    for n in range(0, 3):
                        if tile == goal[m][n]:
                            sum += math.sqrt(math.pow(i - m, 2)  + math.pow(j - n, 2))
        return sum
            

def applyAction(state, action, r, c):
    newValue = deepcopy(state.value)

    if (action == "UP"):
        newValue[r-1][c] , newValue[r][c] = newValue[r][c] , newValue[r-1][c]
        r -= 1
    if (action == "DOWN"):
        newValue[r+1][c] , newValue[r][c] = newValue[r][c] , newValue[r+1][c]
        r += 1
    if (action == "LEFT"):
        newValue[r][c-1] , newValue[r][c] = newValue[r][c] , newValue[r][c-1]
        c -= 1
    if (action == "RIGHT"):
        newValue[r][c+1] , newValue[r][c] = newValue[r][c] , newValue[r][c+1]
        c += 1
    state.depth += 1;
    return State(newValue, action, state, (r,c))



def create_initial_state(arr):
    def get_empty_index(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i,j)
        return (0,0)
        
    return State(arr, None, None, get_empty_index(arr))
