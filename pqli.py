# Creating Priority queue Data structure list

#Creating a class for Priority queue
class PriorityQueue:
    #Creating constructor
    def __init__(self):
        self.mylist = []
        self.count = 0

    #Is empty
    def is_empty(self):
        return len(self.mylist) == 0

    #error message
    def errormessage(self):
        raise Exception("Priority Queue is empty")

    #Push
    def push(self, prioritydata, data):
        self.mylist.append((prioritydata, data))
        self.count += 1
        
    #pop
    def pop(self):
        if not self.is_empty():
            self.count -= 1
            return self.mylist.pop(0)
        else:
            return self.errormessage()
        
    #Peek
    def peek(self):
        if not self.is_empty():
            return self.mylist[0]
        else:
            return self.errormessage()
    #size

    def size(self):
        return self.count
    
    def display(self):
        if not self.is_empty():
            for i in self.mylist:
                print(i)
            print()
        else:
            return self.errormessage()
        
# Create an instance of PriorityQueue
pq = PriorityQueue()

# Test push operation
pq.push(3, "Data 1")
pq.push(1, "Data 2")
pq.push(2, "Data 3")

# Display the elements in the priority queue
pq.display()  # This should print the elements in the priority order

# Test peek operation
print("Peek:", pq.peek())  # This should print the highest priority element without removing it

# Test pop operation
print("Popped:", pq.pop())  # This should remove and return the highest priority element

# Display the elements in the priority queue after pop
pq.display()

# Test size operation
print("Size:", pq.size())  # This should print the size of the priority queue
