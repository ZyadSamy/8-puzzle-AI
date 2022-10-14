from collections import deque

class Frontier:
    def __init__(self, strategy):
        self.strategy = strategy
        self.frontier = deque()

    def pop(self):
        if (self.strategy == "dfs"):
            return self.frontier.pop()
        else:
            return self.frontier.popleft()
    
    def push(self, element):
        self.frontier.append(element)