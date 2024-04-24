#creating queue data structure by extending class list 

#create a class
class Queue(list):
    count = 0
    #is_empty
    def is_empty(self):
        return len(self) == 0
    
    #enqueue
    def enqueue(self,data):
        self.append(data)
        self.count += 1

    #dequeue
    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
            self.count -= 1
    #get_front
    def get_front(self):
        if not self.is_empty():
            return self[0]
        else:
            return 'Queue is empty'

    #get_rear
    def get_rear(self):
        if not self.is_empty():
            return self[-1]
        else:
            return 'Queue is empty'
    
    #size
    def size(self):
        return self.count
    
    #display
    def display(self):
        if not self.is_empty():
            for i in range(len(self)):
                print(self[i], end=" ")
        else:
            return'Queue is empty'
        print()


#Test code 
# Create a queue instance
my_queue = Queue()

# Test is_empty method
print("Is the queue empty?", my_queue.is_empty())  # Output should be True

# Test enqueue method
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# Test display method
print("Queue elements:", end=" ")
my_queue.display()  # Output should be: 10 20 30

# Test get_front and get_rear methods
print("\nFront element of the queue:", my_queue.get_front())  # Output should be 10
print("Rear element of the queue:", my_queue.get_rear())      # Output should be 30

# Test dequeue method
my_queue.dequeue()

# Test size method
print("Size of the queue:", my_queue.size())  # Output should be 2

# Test display method after dequeue
print("Queue elements after dequeue:", end=" ")
my_queue.display()  # Output should be: 20 30


