from collections import deque

class Que():
    def __init__(self):
        self.items = deque()

    def enque(self, item):
        self.items.append(item)

    def deque(self):
        return self.items.popleft()
    
    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

    def is_empty(self):
        return not self.items

    def __str__(self):
        return str(self.items)
    pass

if __name__ == "__main__":
    que = Que()
    print("Running class queue directly.")
    que.enque(5)
    que.enque(7)
    que.enque(100000)
    print(que.size())
    print(que.deque())
    print(que)