#creatig Queue data structure using singly linked list concept

#creating node 
class Node:
    #constructor
    def __init__(self, item=None, nextNode=None):
        self.item = item
        self.next = nextNode

class Queue:
    #constructor
    def __init__(self,head=None):
        self.head = head

    #is_empty
    def is_empty(self):
        return self.head is None
    

    #enqueue
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else: 
            new_node.next = self.head
            self.head = new_node


    #dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            dequeued_item = self.head.item
            self.head = self.head.next
            return dequeued_item

    #get_rear
    def get_rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            return self.head.item

    #get_front
    def get_front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            return current.item


    #size
    def size(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else: 
            count = 1
            current = self.head
            while current.next is not None:
                current = current.next
                count += 1
            return count
            
    #display
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            current = self.head
            while current is not None:
                print(current.item, end= " ")
                current = current.next
            print()

# Create a queue instance
queue = Queue()

# Test enqueue operation
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Display the queue
print("Queue after enqueue operations:")
queue.display()

# Test dequeue operation
dequeued_item = queue.dequeue()
print("Dequeued item:", dequeued_item)

# Display the queue after dequeue operation
print("Queue after dequeue operation:")
queue.display()

# Test get_front and get_rear
print("Front of the queue:", queue.get_front())
print("Rear of the queue:", queue.get_rear())

# Test size
print("Size of the queue:", queue.size())
