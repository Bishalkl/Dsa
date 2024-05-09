# creating a binary search tree 

# creating a class for node 
class Node:

    # constructor
    def __init__(self,item=None):
        self.left = None
        self.item = item
        self.right = None

# create a class for binary search tree 
class BST:

    # constructor
    def __init__(self,root=None):
        self.root = root

    #check empty or not 
    def is_empty(self):
        return self.root is None
    
    # to insert the data 
    def insert(self, data):

        # create a node object insert into data structure
        new_node = Node(data)

        # case: if the root is empty
        if self.is_empty():
            self.root = new_node
            return
        
        #case not empty root 
        current = self.root 

        # loop for traversing 
        while True:
            # case if the data is greater than current
            if data > current.item:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
            
            #case if the data is smaller than current
            if data < current.item:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left



# Drive code 
# Create a binary search tree
bst = BST()

# Insert some data into the tree
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Function to print the tree
def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.item)
        print_tree(node.left, level + 1)

# Print the tree
print("Binary Search Tree:")
print_tree(bst.root)
       

        
        
