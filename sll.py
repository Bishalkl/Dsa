class Node:
    def __init__(self, item=None, nextNode=None):
        self.item = item
        self.next = nextNode

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.start = new_node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def delete_at_first(self):
        if self.is_empty():
            print('Linked list is empty')
            return None
        else:
            self.start= self.start.next

    def delete_at_last(self):
        if self.is_empty():
            print('Linked list is empty')
            return None
        else:
            current = self.start
            previous = None
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None

    def insert_at_index(self, data, index):
        new_node = Node(data)
        if self.is_empty():
            return None
        if index == 0:
            new_node.next = self.start
            self.start = new_node
            return
        count = 0
        temp = self.start
        while temp is not None:
            if count == index - 1:
                new_node.next = temp.next
                temp.next = new_node
                return
            count += 1
            temp = temp.next
        self.insert_at_last(data)

    def searching(self, index):
        if self.is_empty():
            return None
        count = 0
        temp = self.start
        while temp is not None:
            if count == index:
                return temp.item
            count += 1
            temp = temp.next
        return None

    def delete(self, index):
        if self.is_empty():
            print('Linked list is empty')
            return  None
        if index == 0 and self.start is not None:
            self.start = self.start.next
            return
        count = 0
        temp = self.start
        prev = None
        while temp is not None:
            if count == index-1:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
            count += 1

    def __iter__(self):
        return slliterator(self.start)

    def display(self):
        if self.is_empty():
            print('Linked list is empty')
            return None
        current = self.start
        while current is not None:
            print(current.item, end=" ")
            current = current.next
        print()

class slliterator:
    def __init__(self, start=None):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data

# Drive code
# Creating a new linked list
mylist = SLL()

# Inserting elements at the first position
mylist.insert_at_first(15)
mylist.insert_at_first(12)
mylist.insert_at_first(34)

# Displaying the list
print("Displaying list after inserting at first position:")
mylist.display()

# Inserting elements at the last position
mylist.insert_at_last(23)
mylist.insert_at_last(45)

# Displaying the list
print("Displaying list after inserting at last position:")
mylist.display()

# Inserting elements at specific indexes
mylist.insert_at_index(10, 2)
mylist.insert_at_index(50, 5)

# Displaying the list
print("Displaying list after inserting at specific indexes:")
mylist.display()

# Searching for items at various indexes
print("Searching for item at index 2:", mylist.searching(2))
print("Searching for item at index 5:", mylist.searching(5))
print("Searching for item at index 10:", mylist.searching(10))

# Deleting items at specific indexes
mylist.delete(2)
mylist.delete(4)

# Displaying the list after deletion
print("Displaying list after deleting items at specific indexes:")
mylist.display()

# Deleting the first and last items
mylist.delete_at_first()
mylist.delete_at_last()

# Displaying the list after deleting the first and last items
print("Displaying list after deleting first and last items:")
mylist.display()

# Iterating over the list
print("Iterating over the list:")
for item in mylist:
    print(item)

