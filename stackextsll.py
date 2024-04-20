# by extending singly linked list class 

#first create a class for node object
class Node:
    #constructor
    def __init__(self,item=None, nextNode=None):
        self.item = item
        self.next = nextNode

#Now creating a class for singly linked list 
class SLL:
    #constructor
    def __init__(self, head=None):
        self.head = head

    #method to check it is empty
    def is_empty(self):
        return self.head is None

    #method for insertion at first
    def insert_at_first(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        new_node.next =self.head
        self.head = new_node

    #method for insert at last
    def insert_at_last(self, data):
        if self.is_empty():
            self.head = new_node
            return
        new_node = Node(data)
        current = self.head
        while True:
            current = current.next
            if current is None:
                break
        current.next = new_node

    #method for size
    def size(self):
        if self.is_empty():
            print("List is empty")
            return 
        count = 0
        current = self.head
        while True:
            if current is None:
                break
            current = current.next
            count += 1
        return count 
    
    def display(self):
        current = self.head
        while True:
            if current is self.head:
                break
            print(current.item, end=" ")
            current = current.next
        print(current.head.item)
    


#now extending the Singly linked list class in Stack 
class Stack(SLL):
    #constructor
    def __init__(self):
        super().__init__

    def Check_empty(self):
        return self.is_empty()

    #method for push
    def push(self, data):
        return self.insert_at_first(data)

    #method pop
    def pop(self):
        if self.Check_empty():
            print("List is empty")
            return
        popped_item = self.head
        self.head = self.head.next
        return popped_item
    
    #method peek
    def peek(self):
        if self.Check_empty():
            print("list is empty")
            return 
        current = self.head
        while current is not None:
            current = current.next
        return current.item

    #method size
    def size(self):
        return super().size()
    


    # Testing the code
stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

stack.display()

print("Peek:", stack.peek())

print("Pop:", stack.pop())

print("Size:", stack.size())

stack.display()

print("Pop:", stack.pop())
print("Pop:", stack.pop())

print("Size:", stack.size())
    
        


        
