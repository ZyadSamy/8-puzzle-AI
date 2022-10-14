from frontier import Frontier
from state import State


def search(initialState, goalTest, strategy): 
    frontier = Frontier(strategy)
    frontier.push(initialState)
    explored = set()
    
    while len(frontier) > 0:
        state: State = frontier.pop()
        hashedValue = hash(state.value)

        if (hashedValue in explored):
            continue
        explored.add(hashedValue)

        if (goalTest(state.value)):
            print_goal_path(state)
            return True

        for neighbor in state.neighbors():
            if hash(neighbor.value) not in explored:
                frontier.push(neighbor)

    return False


def hash(arr):
    hash = 0
    for row in arr:
        for element in row:
            hash += element
            hash *= 10

    return hash/10


def print_goal_path(state: State):
    goalPath = []
    while state.previousState is not None:
        goalPath.append(state.previousAction)
        state = state.previousState

    goalPath.reverse()
    print(goalPath)
    print(f'Goal path cost: {len(goalPath)}')


def bfs(initialState, goalTest):
    return search(initialState, goalTest, "bfs")

def dfs(initialState, goalTest):
    return search(initialState, goalTest, "dfs")