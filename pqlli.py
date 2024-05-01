class Node:
    #constructor
    def __init__(self, priority=None, item=None):
        self.priority = priority
        self.item = item
        self.next = None

class PriorityQueue:
    #constructor
    def __init__(self, start=None):
        self.start = None

    #error
    def error(self):
        raise Exception("Priority Queue is empty")    

    #is_empty
    def is_empty(self):
        return self.start is None
    
    #push
    def push(self, prioritydata, data):
        new_node = Node(prioritydata, data)
        if self.is_empty() or prioritydata > self.head.priority:
            new_node.next = self.start
            self.start = new_node
        current = self.start
        while current.next is None and current.next.priority >= prioritydata:
            current = current.next
        new_node.next = current.next
        current.next = new_node


    def pop(self):
        if self.is_empty():
            return self.error()
        else:
            popped_item = self.start.item
            self.start = self.start.next
            return popped_item

    # Peek at the top element in the priority queue
    def peek(self):
        if self.is_empty():
            return self.error()
        else:
            return self.start.item

    # Get the size of the priority queue
    def size(self):
        if self.is_empty():
            return self.error()
        else:
            count = 0
            current = self.start
            while current is not None:
                current = current.next
                count += 1
            return count

    # Display the elements in the priority queue
    def display(self):
        if self.is_empty():
            return self.error()
        else:
            current = self.start
            while current is not None:
                print("(" + str(current.priorityitem) + ", " + str(current.item) + ")", end=" ")
                current = current.next
            print()
