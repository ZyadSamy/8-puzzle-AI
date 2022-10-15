from frontier import Stack, Queue
from state import State
from heapq import *

import time

def search(frontier, goalTest): 
    startTime = time.time()
    explored = set()
    
    while len(frontier) > 0:
        state: State = frontier.pop()
        hashedValue = hash(state.value)

        if (hashedValue in explored):
            continue
        explored.add(hashedValue)

        if (goalTest(state.value)):
            print_stats(state, explored, startTime, frontier)
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


def print_stats(state: State, explored, startTime, frontier):
    goalPath = []
    while state.previousState is not None:
        goalPath.append(state.previousAction)
        state = state.previousState

    goalPath.reverse()
    print(goalPath)
    print(f'Goal path cost: {len(goalPath)}')
    print(f'Nodes explored: {len(explored)}')
    print(f'Frontier size: {len(frontier)}')
    # print(f'Max frontier size: {frontier.max()}')
    print(f'running time: {(time.time() - startTime)} s')



def bfs(initialState, goalTest):
    frontier = Queue(initialState)
    return search(frontier, goalTest)

def dfs(initialState, goalTest):
    froniter = Stack(initialState)
    return search(froniter, goalTest)

def astar(initialState, goalTest, heuristic):
    frontier = [initialState]
    return astarhelper(frontier, goalTest, heuristic)



def astarhelper(frontier, goalTest, heuristic):
    startTime = time.time()
    explored = set()

    while len(frontier) > 0:
        state: State = heappop(frontier)
        hashedValue = hash(state.value)

        f_value = state.depth

        if heuristic == "m":
            g_value = state.ManhattenHeuristic()
        else:
            g_value = state.EuclidHeuristic()
        state.cost = f_value + g_value
        if (hashedValue in explored):
            continue
        explored.add(hashedValue)

        if (goalTest(state.value)):
            print_stats(state, explored, startTime, frontier)
            return True

        for neighbor in state.neighbors():
            if hash(neighbor.value) not in explored:
                heappush(frontier,  neighbor)

    return False
