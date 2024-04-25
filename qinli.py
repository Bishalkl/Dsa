class Node:
    def __init__(self, item=None, nextNode=None):
        self.item = item
        self.next = nextNode

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.start = new_node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete_at_first(self):
        if self.is_empty():
            print('Linked list is empty')
            return None
        else:
            self.start = self.start.next

    def delete_at_last(self):
        if self.is_empty():
            print('Linked list is empty')
            return None
        elif self.start.next is None:
            self.start = None
            return
        else:
            current = self.start
            while current.next.next is not None:
                current = current.next
            current.next = None

    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index")
            return
        new_node = Node(data)
        if self.is_empty():
            if index == 0:
                self.start = new_node
            else:
                print("Invalid index")
            return
        if index == 0:
            new_node.next = self.start
            self.start = new_node
            return
        count = 0
        temp = self.start
        while temp is not None:
            if count == index - 1:
                new_node.next = temp.next
                temp.next = new_node
                return
            count += 1
            temp = temp.next
        self.insert_at_last(data)

    def searching(self, index):
        if self.is_empty():
            return None
        count = 0
        temp = self.start
        while temp is not None:
            if count == index:
                return temp.item
            count += 1
            temp = temp.next
        return None

    def delete(self, index):
        if self.is_empty():
            print('Linked list is empty')
            return None
        if index == 0 and self.start is not None:
            self.start = self.start.next
            return
        count = 0
        temp = self.start
        prev = None
        while temp is not None:
            if count == index-1:
                if temp.next is None:
                    prev.next = None
                else:
                    prev.next = temp.next
                break
            prev = temp
            temp = temp.next
            count += 1

    def __iter__(self):
        return slliterator(self.start)

    def display(self):
        if self.is_empty():
            print('Linked list is empty')
            return
        current = self.start
        while current is not None:
            print(current.item, end=" ")
            current = current.next
        print()

class slliterator:
    def __init__(self, start=None):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data

class Queue(SLL):
    def __init__(self):
        super().__init__()

    def is_empty(self):
        return super().is_empty()

    def enqueue(self, data):
        self.insert_at_last(data)

    def dequeue(self):
        self.delete_at_first()

    def get_front(self):
        return self.searching(0)

    def get_rear(self):
        if not self.is_empty():
            return self.searching(self.size() - 1)
        else:
            print("Queue is empty")

    def size(self):
        count = 0
        current = self.start
        while current is not None:
            count += 1
            current = current.next
        return count

# Create a queue instance
queue = Queue()

# Enqueue some data
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Display the queue
queue.display()  # This should print: 1 2 3

# Get the front element
print("Front of the queue:", queue.get_front())  # This should print: 1

# Get the rear element
print("Rear of the queue:", queue.get_rear())    # This should print: 3

# Dequeue an element
queue.dequeue()

# Display the queue after dequeue
queue.display()  # This should print: 2 3
