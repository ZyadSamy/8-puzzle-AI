from frontier import Stack, Queue
from heuristics import *
from state import State
from heapq import *
from file import getStatsPath

import time

def search(frontier, goalTest): 
    startTime = time.time()
    explored = set()
    maxDepth = 0
    
    while len(frontier) > 0:
        state: State = frontier.pop()
        hashedValue = hash(state.value)
        maxDepth = max(maxDepth, state.depth)

        if (hashedValue in explored):
            continue
        explored.add(hashedValue)

        if (goalTest(state.value)):
            print_stats(state, explored, startTime, frontier, maxDepth)
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


def print_stats(state: State, explored, startTime, frontier, maxDepth):
    goalPath = []
    while state.previousState is not None:
        goalPath.append(state.previousAction)
        state = state.previousState

    goalPath.reverse()
    statsPath = getStatsPath
    f = open("Statistics.txt", "a")
    f.write(f"Path to Goal: {goalPath}\n")
    f.write(f'Goal path cost: {len(goalPath)}\n')
    f.write(f'Nodes explored: {len(explored)}\n')
    f.write(f'Frontier size: {len(frontier)}\n')
    f.write(f"Maximum Depth: {maxDepth}\n")
    # f.write(f'Max frontier size: {frontier.max()}')
    f.write(f'running time: {(time.time() - startTime)} s\n')
    f.close()



def bfs(initialState, goalTest):
    frontier = Queue(initialState)
    return search(frontier, goalTest)

def dfs(initialState, goalTest):
    froniter = Stack(initialState)
    return search(froniter, goalTest)

def astar(initialState, goalTest, heuristic = "e"):
    frontier = [initialState]
    if(heuristic == "m" or heuristic == "manhattan"):
        return astarhelper(frontier, goalTest, ManhattenHeuristic)
    else:
        return astarhelper(frontier, goalTest, EuclidHeuristic)


    



def astarhelper(frontier, goalTest, heuristic):
    startTime = time.time()
    explored = set()
    maxDepth = 0

    while len(frontier) > 0:
        state: State = heappop(frontier)
        hashedValue = hash(state.value)
        maxDepth = max(maxDepth, state.depth)

        f_value = state.depth
        
        g_value = heuristic(state)

        state.cost = f_value + g_value
        if (hashedValue in explored):
            continue
        explored.add(hashedValue)

        if (goalTest(state.value)):
            print_stats(state, explored, startTime, frontier, maxDepth)
            return True

        for neighbor in state.neighbors():
            if hash(neighbor.value) not in explored:
                heappush(frontier,  neighbor)

    return False



