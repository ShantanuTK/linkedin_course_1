class Stack():
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return not self.items

    def __len__(self):
        return len(self.items)


def reverse_string():
    string = "dlroWolleH"
    s = Stack()
    reversedString = ""
    for i in range(len(string)):
        s.push(string[i])
    
    while not s.is_empty():
        reversedString += str(s.pop())

    print(reversedString)

if __name__ == '__main__':
    reverse_string()
