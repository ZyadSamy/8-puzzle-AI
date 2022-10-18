from search import bfs, dfs, astar
from goalTest import zero_first_test, zero_last_test
from state import create_initial_state

initialState = create_initial_state([
    [0, 1, 2],
    [3, 5, 4],
    [6, 7, 8]
])

# print (initialState)
bfs(initialState, zero_first_test)
# astar(initialState, zero_first_test, "m")
# astar(initialState, zero_first_test)
