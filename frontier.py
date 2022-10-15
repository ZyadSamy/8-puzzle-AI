from collections import deque

class Queue:
    def __init__(self, *elements):
        self._elements = deque(elements)
        self._maxSize = len(self._elements)

    def __len__(self):
        return len(self._elements)

    def push(self, element):
        self._elements.append(element)
        self._maxSize = max(self._maxSize, len(self._elements))

    def pop(self):
        return self._elements.popleft()

    def max(self):
        return self._maxSize


class Stack(Queue):
    def pop(self):
        return self._elements.pop()