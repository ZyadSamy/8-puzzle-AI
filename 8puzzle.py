from search import bfs, dfs, astar
from goalTest import zero_first_test, zero_last_test
from state import create_initial_state
import sys
from file import *

argumentsLength = len(sys.argv)
arrayString = sys.argv[1]
strategy = sys.argv[2]

if (argumentsLength < 3 or argumentsLength > 4):
    print("Please Enter Valid Arguments (Array, Strategy, Heuristic (if A*))")
    sys.exit()
else:
    if (strategy != "bfs" and strategy != "dfs" and strategy != "a*" and strategy != "all"):
        print("Please Enter Valid Strategy (bfs, dfs, a* + heuristic)")
        sys.exit()
    if (strategy == "a*" and argumentsLength == 3):
        print("Please enter a Valid Heuristic (manhattan for manhattan distance) (euclidean for euclidean distance)")
        sys.exit()
    elif (strategy != "a*" and argumentsLength == 4):
        print("Please Enter Valid Arguments")
        sys.exit()


n = len(arrayString)
if (n != 9):
    print("Please Enter a Valid Array Representation -> ex: 0123456789, 462103857")
    sys.exit()

validatingArray = [0] * 9

for x in arrayString:
    if (int(x) < 0 or int(x) > 8):
        print("Array must contain numbers between 0 and 8")
        sys.exit()

for i in range(9):
    validatingArray[int(arrayString[i])] += 1

for x in validatingArray:
    if (x != 1):
        print("Number in Array is duplicated please make sure there is unique numbers between 0->8.")
        sys.exit()

found = check_file()
if not found:
    f = open("Statistics.txt", "x")

f = open("Statistics.txt", "w")
f.write("All Stats Below")
f.close()


def convert_1d_to_2d(array):

    twodarray = [[0 for i in range(3)] for c in range(3)]
    for i in range(9):
        twodarray[int(i/3)][i % 3] = array[i]
    return twodarray


initialState = convert_1d_to_2d([int(x) for x in arrayString])
initialState = create_initial_state(initialState)

f = open("Statistics.txt", "a")

if (strategy == "bfs"):
    f.write("\n\nBFS Statistics\n\n")
    f.close()
    bfs(initialState, zero_first_test)
elif (strategy == "dfs"):
    f.write("\n\nDFS Statistics\n\n")
    f.close()
    dfs(initialState, zero_first_test)
elif (strategy == "a*"):

    heuristic = sys.argv[3]
    f.write(f"\n\nA* Statistics with {heuristic} heuristic\n")
    f.close()
    astar(initialState, zero_first_test, heuristic)
elif (strategy == "all"):
    f.write("\n\nAll Strategies Statistics Combined\n")
    f.write("\n\nBFS Statistics\n")
    f.close()
    bfs(initialState, zero_first_test)
    f = open("Statistics.txt", "a")
    f.write("\n\nDFS Statistics\n")
    f.close()
    dfs(initialState, zero_first_test)
    f = open("Statistics.txt", "a")
    f.write("\n\nA* Statistics with Manhattan heuristic\n")
    f.close()
    astar(initialState, zero_first_test, "m")
    f = open("Statistics.txt", "a")
    f.write("\n\nA* Statistics with Euclidean heuristic\n")
    f.close()
    astar(initialState, zero_first_test)

print("Done")

# initialState = create_initial_state([
#     [1, 2, 5],
#     [3, 4, 0],
#     [6, 7, 8]
# ])

# # print (initialState)
# dfs(initialState, zero_first_test)
# astar(initialState, zero_first_test, "m")
