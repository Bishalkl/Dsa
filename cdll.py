class Node:

    def __init__(self, item=None):
        self.item = item
        self.prev= None
        self.next = None

class CDLL:

    def __init__(self, head=None):
        self.head = head

    def is_empty(self):
        return self.head is None
    
    #insert at start
    def insert_at_start(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = new_node
            self.head.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = self.head.prev.next
            self.head = new_node


    #method for insert at last
    def insert_at_last(self,data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            new_node.next = self.head
            new_node.prev = self.head.prev
            self.head.prev.next = new_node
            self.head.prev = self.head.prev.next

    #method for insert at index
    def insert_at_index(self,data, index):
        new_node = Node(data)
        if self.is_empty():
            self.head =new_node
            self.head.next = self.head
            self.head.prev = self.head
            return
        
        if index == 0:
            self.insert_at_start(data)
            return
             
        count = 0
        prev = None
        current = self.head
        while True:
            if count == index:
                new_node.next = current
                new_node.prev = current.prev
                current.prev.next = new_node
                current.prev = current.prev.next
            prev = current
            current = current.next
            count += 1
            if current == self.head:
                break

    
    #method to size
    def size(self):
        count = 0
        if self.is_empty():
            return count 
        
        current = self.head
        while True:
            current = current.next
            count += 1
            if current == self.head:
                break
        return count
        
  
    # method for searching
    def searching(self, index):
        if self.is_empty():
            print("The list is empty")
            return
        
        if index == 0:
            print(self.head.item)
            return
        
        if index >= self.size():
            print("Index is out of bound")
            return
        
        count = 0
        current = self.head
        while True:
            if index == count:
                print(current.item)
                break

            current = current.next
            count += 1
            if current == self.head:
                break

    #method of deletion of first
    def delete_at_start(self):
        if self.is_empty():
            print("List is empty")
            return
        
        if self.size() == 0:
            self.head = None
            return
        
        self.head.prev.next = self.head.next 
        self.head = self.head.next


    #method of deletion of last 
    def delete_at_last(self):

        if self.is_empty():
            print("List is empty")
            return
        
        if self.size() == 1:
            self.head = None
            return
        
        self.head.prev.prev.next = self.head
        self.head.prev = self.head.prev.prev


     #method of deletion of index
    def delete_at_index(self,index):
        if self.is_empty():
            print("list is empty")
            return 
        
        if index == 0:
            self.delete_at_start()
            return
        
        if self.size() == index - 1:
            self.delete_at_last()
            return
        
        count = 0
        prev = None
        current = self.head
        while True:
            if count == index:
                prev.next = current.next
                current.next.prev = prev
                break
            prev = current
            current = current.next
            count +=1

            if current == self.head:
                break

    # method for display
    def display(self):
        if self.is_empty():
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.item, end=" ")
            current = current.next
            if current == self.head:
                break
        print()

    


# Create an empty circular doubly linked list
mylist = CDLL()

# Test insert at start
mylist.insert_at_start(1)
mylist.insert_at_start(2)
mylist.insert_at_start(3)
mylist.display()  # Output: 3 2 1

# Test insert at last
mylist.insert_at_last(4)
mylist.insert_at_last(5)
mylist.display()  # Output: 3 2 1 4 5

# Test insert at index
mylist.insert_at_index(10, 2)
mylist.insert_at_index(20, 0)
mylist.display()  # Output: 20 3 10 2 1 4 5

# Test size
print("Size:", mylist.size())  # Output: 7

# Test searching
print("Element at index 3:", end=" ")
mylist.searching(3)  # Output: 2

# Test delete at start
mylist.delete_at_start()
mylist.display()  # Output: 3 10 2 1 4 5

# Test delete at last
mylist.delete_at_last()
mylist.display()  # Output: 3 10 2 1 4

# Test delete at index
mylist.delete_at_index(2)
mylist.display()  # Output: 3 10 1 4

