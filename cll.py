class Node:
    def __init__(self, item=None):
        self.item = item
        self.next = None

class CLL:
    def __init__(self):
        self.tail = None
    
    def is_empty(self):
        return self.tail is None
    
    def insert_at_start(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node


    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node



    def searching(self, data):
        if self.is_empty():
            print("List is empty")
            return
        count = 0
        current = self.tail.next
        while current is not self.tail:
            if data == current.item:
                print(count)
                break
            current = current.next
            count += 1


    def insert_at_index(self, data, index):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = self.tail.next
            self.tail.next = new_node
            return 
        current = self.tail.next
        count = 0
        prev = None
        while current is not self.tail:
            if count == index:
                new_node.next = prev.next
                prev.next = new_node
            prev = current
            current = current.next
            count += 1


    def delete_at_start(self):
        if self.is_empty():
            print("List is empty")
            return 
        self.tail.next =self.tail.next.next

    def delete_at_last(self):
        if self.is_empty():
            print("List is empty")
        current = self.tail.next
        prev = None
        while current is not self.tail:
            prev = current
            current = current.next
        prev.next = current.next
        self.tail = prev
                
    def delete_at_index(self, index):
        if self.is_empty():
            print("List is empty")
            return
        
        if index == 0:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                self.tail.next = self.tail.next.next
            return
        
        prev = None
        count = 0
        current = self.tail.next
        while current is not self.tail:
            if count == index:
                prev.next = current.next
                break
            prev = current 
            current = current.next
            count += 1 
            


    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.tail.next
        while True:
            print(current.item, end=" ")
            current = current.next
            if current == self.tail:
                break
        print(self.tail.item) 

    
            

            

# Testing the code
mylist = CLL()
mylist.insert_at_start(23)
mylist.insert_at_start(45)
mylist.insert_at_start(34)
mylist.insert_at_last(10)
mylist.insert_at_last(34)
mylist.insert_at_last(34)
mylist.display()
mylist.delete_at_index(1)
mylist.display()
