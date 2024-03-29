class Queue:
    def __init__(self):
        self.items = []

    def examine(self):
        return self.items

    def enqueue(self, item):
        return self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def q_length(self):
        return len(self.items)
