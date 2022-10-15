from search import bfs, dfs
from goalTest import zero_first_test, zero_last_test
from state import create_initial_state


initialState = create_initial_state([
    [1,2,5],
    [3,4,0],
    [6,7,8]
])


# print (initialState)
dfs(initialState, zero_first_test)