from search import bfs
from goalTest import zero_first_test, zero_last_test
from state import create_initial_state


initialState = create_initial_state([
    [3,1,2],
    [6,4,5],
    [0,7,8]
])

print(bfs(initialState, zero_first_test))
#print(bfs(initialState, zero_last_test))