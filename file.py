import os
import time


def check_file():
    statsPath = get_stats_path()
    return os.path.isfile(statsPath)


def get_stats_path():
    return os.sep.join([os.getcwd(), "Statistics.txt"])


def print_stats_to_file(state, explored, startTime, frontier, maxDepth):
    goalPath = []
    while state.previousState is not None:
        goalPath.append(state.previousAction)
        state = state.previousState

    goalPath.reverse()
    f = open("Statistics.txt", "a")
    f.write(f"Path to Goal: {goalPath}\n")
    f.write(f'Goal path cost: {len(goalPath)}\n')
    f.write(f'Nodes explored: {len(explored)}\n')
    f.write(f'Frontier size: {len(frontier)}\n')
    f.write(f"Maximum Depth: {maxDepth}\n")
    # f.write(f'Max frontier size: {frontier.max()}')
    f.write(f'running time: {(time.time() - startTime)} s\n')
    f.close()
