class Node:
    def __init__(self, item=None, nextNode=None):
        self.item = item
        self.next = nextNode

class SLL:
    def __init__(self, start=None):
        self.start = start

    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        temp = self.start
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def insert_at_index(self, data, index):
        new_node = Node(data)
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
            count += 1
            temp = temp.next

    def searching(self, index):
        count = 0
        temp = self.start
        while temp is not None:
            if count == index:
                return temp.item
            count += 1
            temp = temp.next
        return None

    def delete(self, index):
        if index == 0 and self.start is not None:
            self.start = self.start.next
            return
        count = 0
        temp = self.start
        prev = None
        while temp is not None:
            if count == index:
                prev.next = temp.next
                break
            prev = temp
            temp = temp.next
            count += 1

    def __iter__(self):
        return slliterator(self.start)

    def display(self):
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
mylist = SLL()
mylist.insert_at_first(15)
mylist.insert_at_first(12)
mylist.insert_at_first(34)
mylist.insert_at_first(15)
mylist.insert_at_first(12)
mylist.insert_at_first(34)
mylist.insert_at_last(23)
mylist.insert_at_last(23)
mylist.insert_at_index(10, 2)

print("Displaying list:")
mylist.display()

print("Searching for item at index 3:", mylist.searching(3))

print("Deleting item at index 1")
mylist.delete(1)

print("Displaying list after deletion:")
mylist.display()

print("Iterating over the list:")
for item in mylist:
    print(item)
