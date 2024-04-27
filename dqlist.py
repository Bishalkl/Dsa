#Creating data structure of dequeue using list

class Dequeue:
    #constructor
    def __init__(self):
        self.mylist = []
        self.count = 0

    #check the dsa is empty or not
    def is_empty(self):
        return len(self.mylist) == 0
    
    # Insert at the Rear
    def insert_at_Front(self, data):
        self.mylist.append(data)
        self.count += 1

    #Insert at the front
    def insert_at_Rear(self, data):
        if self.is_empty():
            self.insert_at_Front()
        else:
            self.mylist.insert(0, data)
            self.count += 1

    #Delete from the front
    def delete_at_Front(self):
        if self.is_empty():
            print("Dequeue is empty")
            return
        else:
            self.mylist.pop()
            self.count -= 1

    #Delete from the Rear
    def delete_at_Rear(self):
        if self.is_empty():
            print("Dequeue is empty")
            return
        else:
            self.mylist.pop(0)
            self.count -= 1
            
    #size of the data structure
    def size(self):
        return self.count
    
    #display
    def display(self):
        for item in self.mylist:
            print(item, end= " ")
        print()

# Create a Dequeue object
deque = Dequeue()

# Insert elements at the front
deque.insert_at_Front(1)
deque.insert_at_Front(2)
deque.insert_at_Front(3)

# Display the deque
print("Deque after inserting at front:")
deque.display()  # Should print: 3 2 1

# Insert elements at the rear
deque.insert_at_Rear(4)
deque.insert_at_Rear(5)

# Display the deque
print("Deque after inserting at rear:")
deque.display()  # Should print: 3 2 1 4 5

# Delete elements from the front
deque.delete_at_Front()
deque.delete_at_Front()

# Display the deque
print("Deque after deleting from front:")
deque.display()  # Should print: 1 4 5

# Delete elements from the rear
deque.delete_at_Rear()

# Display the deque
print("Deque after deleting from rear:")
deque.display()  # Should print: 1 4


deque.size()
