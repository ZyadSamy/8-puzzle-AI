from copy import deepcopy


class State:
    def __init__(self, val, preAction, preState, emptyIndex, depth=0):
        self.value = val
        self.previousAction = preAction
        self.previousState = preState
        self.emptyIndex = emptyIndex
        self.depth = depth
        self.cost = 0

    def __str__(self):
        line = f'-------\n'
        out = ""
        out += line
        for r in self.value:
            out += f'|{r[0]}|{r[1]}|{r[2]}|\n'
            out += line
        return out

    def __gt__(self, state):
        return self.cost > state.cost

    def neighbors(self):
        (row, col) = self.emptyIndex
        actions = []
        neighbors = []

        if (col > 0):
            actions.append("LEFT")

        if (row > 0):
            actions.append("UP")

        if (col < 2):
            actions.append("RIGHT")

        if (row < 2):
            actions.append("DOWN")

        for action in actions:
            neighbors.append(apply_action(self, action, row, col))

        return neighbors


def apply_action(state, action, r, c):
    newValue = deepcopy(state.value)

    if (action == "UP"):
        newValue[r-1][c], newValue[r][c] = newValue[r][c], newValue[r-1][c]
        r -= 1
    if (action == "DOWN"):
        newValue[r+1][c], newValue[r][c] = newValue[r][c], newValue[r+1][c]
        r += 1
    if (action == "LEFT"):
        newValue[r][c-1], newValue[r][c] = newValue[r][c], newValue[r][c-1]
        c -= 1
    if (action == "RIGHT"):
        newValue[r][c+1], newValue[r][c] = newValue[r][c], newValue[r][c+1]
        c += 1
    return State(newValue, action, state, (r, c), state.depth + 1)


def create_initial_state(arr):
    def get_empty_index(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)
        return (0, 0)

    return State(arr, None, None, get_empty_index(arr))
