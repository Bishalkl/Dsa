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

        
        #method for deletion
            def delete(self, data):
                if self.is_empty():
                    print("Your binary search tree is empty")
                    return
                
                # create a traversinng first 
                previous = None
                current = self.root

                # loop for traversing 
                while True:
                    # case if the data is equal and found the data 
                    if data  == current.item:
                        # case with no children
                        if current.left is None and current.right is None:
                            # case right is data 
                            if previous.right.item == current.item:
                                previous.right = None
                                current = previous
                                break

                            # case left is data
                            elif previous.left.item == current.item:
                                previous.left = None
                                current.previous
                                break

                        # case with one children
                        elif current.right is not None or current.left is not None:
                            pass
                        # case wit two children

                    


                
                    # case if the data is greater 
                    elif data > current.item:
                        previous = current
                        current = current.right

                    elif data < current.item:
                        previous = current
                        current = current.left



                        




                
                

                
                
                









            










       

        
        
