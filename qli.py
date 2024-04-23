#using by list to make a queue 
#enqueue
#dequeue
#is_empty
#get_front
#get_rear


#creating class for queue
class Queue:
    # creating a construction
    def __init__(self):
        self.item = []
        self.count = 0

    #is_empty
    def is_empty(self):
        return len(self.item) == 0

    #enqueue
    def enqueue(self, data):
        self.item.append(data)
        self.count += 1

    #dequeue
    def dequeue(self):
        if not self.is_empty():
            self.item.pop(0)
            self.count -= 1
            

    #get_front
    def get_front(self):
        if not self.is_empty():
            return self.item[0]
        else:
            return 'Queue is empty'

    #get_rear(self):
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            return 'Queue is empty'
        
    #get_size:
    def get_size(self):
        return self.count
        
    #display
    def display(self):
        if not self.is_empty():
            for i in range(len(self.item)):
                print(self.item[i])
        else:
            return 'Queue is empty'

        
# Create a Queue object
queue = Queue()

# Check if the queue is empty
print("Is queue empty?", queue.is_empty())  # Output should be True

# Enqueue some elements
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Check the front and rear elements
print("Front of the queue:", queue.get_front())  # Output should be 1
print("Rear of the queue:", queue.get_rear())    # Output should be 3

# Get the size of the queue
print("Size of the queue:", queue.get_size())    # Output should be 3

# Display the queue
print("Queue elements:")
queue.display()  # Output should be: 1 2 3

# Dequeue an element
queue.dequeue()

# Check the front element after dequeue
print("Front of the queue after dequeue:", queue.get_front())  # Output should be 2

# Display the queue after dequeue
print("Queue elements after dequeue:")
queue.display()  # Output should be: 2 3

# Get the size of the queue after dequeue
print("Size of the queue after dequeue:", queue.get_size())    # Output should be 2


