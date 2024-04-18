# creating a  class for node object 
class Node:
    # constructor
    def __init__(self, item=None):
        self.item = item
        self.prev = None
        self.next = None
    
# Creating a class for Doubly linked list object
class DLL:
    # constructor
    def __init__(self, head=None):
        self.head = head

    #creating method add node in at first
    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.prev = None
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


    #creating method add node in at last
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.prev = None
            new_node.next= None
            self.head = new_node
            return
        current = self.head    #for treverse
        while current.next is not None:
            current = current.next
        new_node.next = None
        new_node.prev = current
        current.next= new_node

    #creating method to insert a node according to index
    def insert_at_index(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.prev= None
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head # for treverse
        count = 0
        while current.next is not None:
            if count == index - 1:
                new_node.prev = current
                new_node.next = current.next
                current.next = new_node
            current = current.next
            count += 1
        print()

    #creating method to search the index according to index 
    def searching(self, index):
        count = 0
        current = self.head
        while current.next is not None:
            if count == index:
                print(current.item)
            current = current.next
            count += 1

    #creating method to delete at first
    def delete_at_first(self):
        if self.head == None:
            return
        
        if self.head.prev == None:
            self.head = None
            return 

        if self.head.prev == None :
            self.head = self.head.next
            self.head.prev = None

    
    #creating method to delete at last
    def delete_at_last(self):
        if self.head is None:
            return 
        
        if self.head.next is None:
            self.head = None
            return
        
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next
        previous.next= None



    #creatig method to delete at index
    def delete_at_index(self, index):

        if index == 0:
            self.head = None
            return 
    
        count = 0
        current = self.head
        previous = None
        while current.next is not None:
            if count == index:
                previous.next = current.next
                current.prev = previous
                break
            previous = current
            current = current.next
            count += 1

    def display(self):
        current = self.head
        while current is not None:
            print(current.item, end=" ")
            current = current.next
        print()



# Drive Code
mylist = DLL()
mylist.insert_at_first(5)
mylist.insert_at_first(3)
mylist.insert_at_last(1)
mylist.insert_at_last(2)
mylist.insert_at_last(4)
mylist.insert_at_index(10, 1)
mylist.searching(1)
mylist.display()
mylist.delete_at_index(2)
mylist.display()