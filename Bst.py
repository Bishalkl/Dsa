# Creating a Binary search tree
# create a node
class Node:
    # constructor
    def __init__(self, item=None):
        self.left = None
        self.item = item
        self.right = None

# create a class for binary search tree
class BST:
    # constructor
    def __init__(self, root=None):
        self.root = root

    # method for empty
    def is_empty(self):
        return self.root is None
    
    # method for insertion
    def insert(self, data):
        # create a node object
        new_node = Node(data)

        # first case: is empty
        if self.is_empty():
            self.root = new_node
            return
        

        current = self.root


        while True:
            # case if data is greate 
            if data >= current.item:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

            elif data < current.item:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left


            
# Test your code
if __name__ == "__main__":
    # Create an instance of the BST class
    bst = BST()

    # Insert some data into the binary search tree
    data_list = [10, 5, 15, 3, 7, 12, 17]
    for data in data_list:
        bst.insert(data)

    # Print the contents of the binary search tree
    def inorder_traversal(node):
        if node is not None:
            inorder_traversal(node.left)
            print(node.item, end=" ")
            inorder_traversal(node.right)

    print("Inorder traversal of the binary search tree:")
    inorder_traversal(bst.root)            


                


            




        

