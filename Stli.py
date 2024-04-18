
# creating a class for stack by using list() of python

class Stack:
    # constructor
    def __init__(self):
        self.list = []

    #method for is_empty 
    def is_empty(self):
        return self.list is None
    
    #method for push:
    def push(self,data):
        self.list.append(data)

    #method for pop
    def pop(self):
        if self.is_empty():
            print("Your stack is empty")
            return None
        return self.list.pop()

        
    #method for peek
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        print(self.list[-1])
    

    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        for i in range(0, len(self.list)):
            print(self.list[i], end=" ")
        print()

        
#test code
mylist = Stack()
mylist.push(23)
mylist.push(45)
mylist.push(67)
mylist.pop()
mylist.peek()
mylist.display()