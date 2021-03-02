class ListQueue:
    def __init__(self):
        self.items = []
        self.size = 0

    def __len__(self):
        return self.size

    def enqueue(self, data):
        self.items.insert(0, data)
        self.size += 1

    def dequeue(self):
        if len(self) > 0:
            data = self.items.pop()
            self.size -= 1
            return data
        return None