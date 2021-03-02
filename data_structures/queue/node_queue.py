class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

class NodeQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def __len__(self):
        return self.size

    def __del__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.previous = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1

    
    def dequeue(self):
        data = None
        if self.size == 1:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size -=1
        elif self.size > 1:
            data = self.head.data
            self.head = self.head.next
            self.head.previous = None
            self.size -= 1
        return data
