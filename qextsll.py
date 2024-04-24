# creatig queue datastructure by extending singly linked list 
from sll import SLL, Node

class Queue:
    #constructor
    def __init__(self):
        self.sll = SLL()

    #is_empty
    def is_empty(self):
        return self.sll.is_empty()

    #enqueue
    def enqueue(self, data):
        self.sll.insert_at_first(data)

    #dequeue
    def dequeue(self):
        if not self.is_empty():
            self.sll.delete_at_first()
        else:
            return 'Queue is empty'

        

    #get_rear
    def get_front(self):
        if not self.is_empty():
            return self.sll.searching(self.size() - 1)
        else:
            return 'Queue is empty'
        

      #get_front
    def get_rear(self):
        if not self.is_empty():
            return self.sll.searching(0)
        else:
            return 'Queue is empty'
    

    #get_size
    def size(self):
        if not self.is_empty():
            count = 0
            current = self.sll.start
            while current is not None:
                current = current.next
                count += 1
            return count
        else:
            return 'Queue is empty'
        

# Create a Queue instance
q = Queue()

# Test is_empty() method
print("Is queue empty?", q.is_empty())  # Output should be True

# Test enqueue() method
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Test get_front() and get_rear() methods
print("Front of the queue:", q.get_front())  # Output should be 1
print("Rear of the queue:", q.get_rear())    # Output should be 3

# Test size() method
print("Size of the queue:", q.size())  # Output should be 3

# Test dequeue() method
print("Dequeue:", q.dequeue())  # Output should be 1

# Test get_front() after dequeue
print("Front of the queue after dequeue:", q.get_front())  # Output should be 2

# Test size() method after dequeue
print("Size of the queue after dequeue:", q.size())  # Output should be 2

