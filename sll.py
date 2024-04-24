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
