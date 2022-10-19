from file import print_stats_to_file
from frontier import Stack, Queue, Heap
from heuristics import *
from heapq import *

import time

# Checks if Initial state entered is solvable or not.
def Solvable(initialState) :
    inversions = 0
    for i in range(9):
        for j in range(i+1, 9):
            if initialState[i] == 0 or initialState[j] == 0 :
                continue
            if initialState[i] > initialState[j]:
                inversions +=1
    return inversions % 2 == 0
        


# DFS AND BFS
# -----------
def search(frontier, initialState, goalTest):
    explored = set()
    frontierSet = set()

    # Frontier varies depending on the type of search used (Stack or Queue)
    frontier.push(initialState)
    frontierSet.add(hash(initialState.value))

    startTime = time.time()
    maxDepth = 0

    while len(frontier) > 0:
        state = frontier.pop()
        stateHash = hash(state.value)

        frontierSet.remove(stateHash)
        explored.add(stateHash)
        maxDepth = max(maxDepth, state.depth)

        if (goalTest(state.value)):
            print_stats_to_file(state, explored, startTime, frontier, maxDepth)
            return True

        for neighbor in state.neighbors():
            neighborHash = hash(neighbor.value)

            if neighborHash not in explored and neighborHash not in frontierSet:
                frontier.push(neighbor)
                frontierSet.add(neighborHash)

    print(f'No possible answer, explored: {len(explored)}')
    return False


def hash(arr):
    hash = 0
    for row in arr:
        for element in row:
            hash *= 10
            hash += element
    return hash


def bfs(initialState, goalTest):
    frontier = Queue()
    return search(frontier, initialState, goalTest)


def dfs(initialState, goalTest):
    frontier = Stack()
    return search(frontier, initialState, goalTest)


def astar(initialState, goalTest, heuristic="e"):
    frontier = Heap()
    if (heuristic == "m" or heuristic == "manhattan"):
        return astarhelper(frontier, initialState, goalTest, ManhattenHeuristic)
    elif (heuristic == "e" or heuristic == "eucildean"):
        return astarhelper(frontier, initialState, goalTest, EuclidHeuristic)

# A*
def astarhelper(frontier, initialState, goalTest, heuristic):
    explored = set()
    frontier.push(initialState)

    startTime = time.time()
    maxDepth = 0

    while len(frontier) > 0:
        state = frontier.pop()
        stateHash = hash(state.value)

        if (stateHash in explored):
            continue

        explored.add(stateHash)
        maxDepth = max(maxDepth, state.depth)

        if (goalTest(state.value)):
            print_stats_to_file(state, explored, startTime, frontier, maxDepth)
            return True

        for neighbor in state.neighbors():
            neighborHash = hash(neighbor.value)

            if neighborHash not in explored:
                f_value = neighbor.depth
                g_value = heuristic(neighbor)
                neighbor.cost = f_value + g_value
                frontier.push(neighbor)

    print(f'No possible answer, explored: {len(explored)}')
    return False
