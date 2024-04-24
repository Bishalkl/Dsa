# creatig queue datastructure by extending singly linked list 
from sll import SLL, Node

class Queue:
    #constructor
    def __init__(self):
        self.sll = SLL()

    #is_empty
    def is_empty(self):
        return self.is_empty()

    #enqueue
    def enqueue(self, data):
        self.sll.insert_at_first(data)

    #dequeue
    def dequeue(self):
        if not self.is_empty():
            self.sll.delete_at_first()
        else:
            return 'Queue is empty'
        
    #get_front
    def get_front(self):
        if not self.is_empty():
            current = self.start
            while current is not None:
                current = current.next
            return current.item
        else:
            return 'Queue is empty'
        

    #get_rear
    def get_rear(self):
        if not self.is_empty():
            return self.start
        else:
            return 'Queue is empty'
        

    #get_size
    def size(self):
        if not self.is_empty():
            count = 1
            current = self.start
            while current is not None:
                current = current.next
                count += 1
            return count
        else:
            return 'Queue is empty'