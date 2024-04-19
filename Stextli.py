# by extending list class 

#creating class Stack and extend list class 
class Stack(list):

    #method for check empty
    def is_empty(self):
        return len(self) == 0
    
    #method for push 
    def push(self, item):
        return self.append(item)
    
    #method for pop
    def pop(self):
        return super().pop()
    
    #method for size
    def size(self):
        if self.is_empty():
            print("list is empty")
            return None
        return len(self)
    
    #method peek
    def peek(self):
        if self.is_empty():
            print("List is empty")
            return None
        print(self[-1])    
        
    #method display
    def display(self):
        if self.is_empty():
            print("List is empty")
            return None
        for item in self:
            print(item, end=" ")
        print()
        

# test code
mylist = Stack()
mylist.push(12)
mylist.push(45)
mylist.peek()
mylist.display()
    
    