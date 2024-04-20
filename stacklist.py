


# using linked list class with singly linked list

class Node: 
    def __init__(self,item=None, next=None):
        self.item  = item
        self.next = next

class Stack:  

    def __init__(self, head=None):
        self.head = head



    def is_empty(self):
        return self.head is None
    
    
    def push(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return None
        else:
            new_node.next = self.head
            self.head = new_node



        
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped_item = self.head.item
        self.head = self.head.next
        print(popped_item)



    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print(self.head.item)




    def size(self):
        if self.is_empty():
            print("Stack is empty")
        current = self.head
        count = 1
        while True:
            current = current.next
            count += 1
            if current.next is None:
                break
        print(count)




    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        current = self.head
        while True:
            if current is None:
                break
            print(current.item, end=" ")
            current = current.next
        print()
        
        

# Creating a stack
stack = Stack()

# Pushing elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)

# Displaying the stack
print("Stack elements:")
stack.display()  # Output: 3 2 1

# Getting the size of the stack
print("Size of the stack:")
stack.size()  # Output: 3

# Peeking at the top element of the stack
print("Top element of the stack:")
stack.peek()  # Output: 3

# Popping an element from the stack
print("Popped element from the stack:")
stack.pop()  # Output: 3

# Displaying the updated stack
print("Updated stack elements:")
stack.display()  # Output: 2 1

# Getting the updated size of the stack
print("Updated size of the stack:")
stack.size()  # Output: 2





