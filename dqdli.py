#Creating a dequeue data structure using doubly linked list concept

#create a node object 
class Node:
    #constructor
    def __init__(self, item=None):
        self.prev = None
        self.item = item
        self.next = None

#create a Dequeue data structure
class Dequeue:
    #constructor
    def __init__(self, head= None):
        self.head = head

    #is_empty
    def is_empty(self):
        return self.head is None

    #insert_at_Rear
    def insert_at_Rear(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        

    #insert_at_Front
    def insert_at_Front(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = None
            new_node.prev = None
            self.head = new_node
            return
        else:
            current  = self.head
            while current.next is not None:
                current = current.next
            new_node.next = None
            new_node.prev = current
            current.next = new_node
            


    #Delete_at_Rear
    def delete_at_Rear(self):
        if self.is_empty():
            print("Dequeue is empty")
            return
        else:
            self.head = self.head.next
            self.head.next.prev = None

    #Delete_at_Front
    def delete_at_Front(self):
        if self.is_empty():
            print("Dequeue is empty")
            return 
        else:
            current = self.head
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
                

    #size
    def size(self):
        count  = 0
        if self.is_empty():
            print("Dequeue is empty")
            return 
        else:
            current = self.head
            while current is not None:
                current = current.next
                count += 1
            return count
        


    #display
    def display(self):
        if self.is_empty():
            print("Dequeue is empty")
            return
        else:
            current = self.head
            while current is not None:
                print(current.item, end= " ")
                current = current.next
            print()

# Create a deque instance
deque = Dequeue()

# Test insertion at the rear
deque.insert_at_Rear(1)
deque.insert_at_Rear(2)
deque.insert_at_Rear(3)

# Display the deque
print("Deque after inserting at rear:")
deque.display()  # Output: 3 2 1

# Test insertion at the front
deque.insert_at_Front(4)
deque.insert_at_Front(5)

# Display the deque
print("Deque after inserting at front:")
deque.display()  # Output: 3 2 1 4 5

# Test deletion from the rear
deque.delete_at_Rear()

# Display the deque
print("Deque after deleting from rear:")
deque.display()  # Output: 2 1 4 5

# Test deletion from the front
deque.delete_at_Front()

# Display the deque
print("Deque after deleting from front:")
deque.display()  # Output: 2 1 4

# Get the size of the deque
print("Size of the deque:", deque.size())  # Output: 3
