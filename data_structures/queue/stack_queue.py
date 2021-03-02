class StackQueue:
    def __init__(self):
        self.inbound_stack = []
        self.outbound_stack = []
        self.size = 0

    def __len__(self):
        return self.size
    
    def enqueue(self, data):
        self.inbound_stack.append(data)
        self.size += 1

    def dequeue(self):
        if not self.outbound_stack and not self.inbound_stack:
            return None
        elif not self.outbound_stack:
            while self.inbound_stack:
                self.outbound_stack.append(self.inbound_stack.pop())
        self.size -= 1
        return self.outbound_stack.pop()
