class Stack:
    def __init__(self):
        self.items = []

    def examine(self):
        return self.items

    def stack_length(self):
        return len(self.items)

    def add_item(self, item):
        return self.items.insert(0, item)

    def remove_item(self):
        return self.items.pop(0)




s = Stack()
print s.examine
s.add_item("b")
s.add_item(2)
s.add_item("c")
s.add_item("Billy")
print s.examine
s.remove_item()
print s.examine
s.remove_item()
print s.examine
