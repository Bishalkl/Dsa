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
    

    # method for implement inorder traversal
    def in_order_traversal(self):
        # if the tree is empty
        if self.root is None:
            return None
        
        # create a travese variable 
        traverse = self.root
        previous = None

        # loop for traverse
        while True:
            
            if traverse.item is not None: 
                print(traverse.item, end=" ")
                traverse = traverse.left
            else: 
                print(traverse.right.item)
                traverse = traverse.right
                

            






                








            

            

