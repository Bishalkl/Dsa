# Assignnment-20: Binary Search Tree part-1

# create a class for nnode 
class Node:

    # constructor
    def __init__(self,item=None):
        self.left = None
        self.item = item
        self.right= None

# create a class for binary search tree 
class BST:

    # constructor
    def __init__(self, root=None):
        self.root = root


    # method for insert a data
    def insert(self, data):

        # create node object
        new_node = Node(data)

        # case one tree is empty
        if self.root is None:
            self.root = new_node
            return
        
        # case for insert with traversing according to the condition and rules
        traverse = self.root

        # loop for traverse 
        while True:

            # case one if the data is smaller than self.root
            if data < traverse.item:
                if traverse.left is None:
                    traverse.left = new_node
                    break
                else:
                    traverse = traverse.left

            # case two if the data is greater than self.root
            elif data > traverse.item:
                if traverse.right is None:
                    traverse.right = new_node
                    break
                else: 
                    traverse = traverse.right
            
            else:
                print("Your data is not valid")


    #method for searching 
    def searching(self, data):

        # if tree is empty
        if self.root is None:
            print("Your tree is empty")
            return None

        # create a traverse variable 
        traverse = self.root

        # loop for traverse
        while traverse:

            # if data is smaller
            if data < traverse.item:
                traverse = traverse.left

            # if data is greater
            elif data > traverse.item:
                traverse = traverse.right
            
            # otherwise
            else:
                return traverse.item 
              
        return None

# Drive code 
# Create a binary search tree instance
bst = BST()

# Insert some elements into the tree
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(8)

# Test searching functionality
print("Searching for 4:", bst.searching(4))  # Output: 4
print("Searching for 10:", bst.searching(10))  # Output: None

                








            

            

