# this creates a single node
class Node(object):
    def __int__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class Linked_List(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)

        # points next at current head, at 'beginning' of list
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        counter = 0
        while current:
            count += 1
            current = current.get_next()
        return counter

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Node not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == current:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Node not int list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())