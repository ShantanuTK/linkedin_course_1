import heapq
class PriorityQue():
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)

    
if __name__ == '__main__':
    priorityQue = PriorityQue()
    print(priorityQue)
    print(priorityQue.is_empty())

    # insert items
    priorityQue.put("eat", 3)
    priorityQue.put("code", 1)
    priorityQue.put("sleep", 2)
    print()
    print(priorityQue)

    priorityQue.get()
    print()
    print(priorityQue)
