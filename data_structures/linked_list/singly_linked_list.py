class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
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
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
        else:
            self.head = node
        self.size += 1

    def prepend(self, data):
        node = Node(data)
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node
        self.size += 1

    def remove_head(self):
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data
        return None

    def remove_tail(self):
        if self.head == None:
            return None
        elif self.head.next == None:
            data = self.head.data
            self.head = None
            self.size -= 1
            return data
        else:
            second_last = self.head
            while second_last.next.next:
                second_last = second_last.next
            data = second_last.next.data
            second_last.next = None
            self.size -= 1
            return data


    def remove(self, data):
        current = self.head
        previous = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    self.size -= 1
                    return data
                elif current.next == None:
                    previous.next = None
                    self.size -= 1
                    return data
                else:
                    previous.next = current.next
                    self.size -= 1
                    return data
            previous = current
            current = current.next
        return None
    
    def reverse(self):
        previous = None
        current = self.head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

