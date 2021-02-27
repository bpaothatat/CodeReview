class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None

    def __str__(self):
        return str(self.data)

class DoublyLinkedList():
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
        
    def __str__(self):
        return str(list(self))

    def __del__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return len(self) == 0
    
    def contains(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def prepend(self, data):
        node = Node(data)
        if self.head:
            self.head.previous = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def remove_head(self):
        if self.head != None:
            data = self.head.data
            self.head = self.head.next
            if self.head != None:
                self.head.previous = None
            self.size -= 1
            return data
        return None

    def remove_tail(self):
        if self.head == None:
            return None 
        elif self.head.next == None:
            data = self.head.data
            self.head = None
            self.tail = None
            self.size -= 1
            return data
        else:
            data = self.tail.data
            self.tail = self.tail.previous
            self.tail.next = None
            self.size -= 1
            return data 


    def remove(self, data):
        if self.head != None:
            if self.head.data == data:
                self.head = self.head.next
                self.head.previous = None
                self.size -= 1
                return data
            elif self.tail.data == data:
                self.tail = self.tail.previous
                self.tail.next = None
                self.size -= 1
                return data
            else:
                current = self.head
                while current:
                    if current.data == data:
                        current.previous.next = current.next
                        current.next.previous = current.previous
                        self.size -= 1
                        return data
                    current = current.next
        return None