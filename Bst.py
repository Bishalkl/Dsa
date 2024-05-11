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
        self.root = self._insert_recursive(self.root, data)
    # method for recursive functin for insertion 
    def _insert_recursive(self, root, data):
        # first case if the code is empty
        if self.root is None:
            return Node(data)
        # seconnd case if the data is greater
        if data < root.item:
            root.left = self._insert_recursive(root.left, data)

        else:
            root.right = self._insert_recursive(root.right, data)

        return root
    
    # method for searching 
    def searching(self, data):
        return self._search_recursive(self.root, data)
    # method for recursive function for searching 
    def _searching_recursive(self,root,data):
        # first case if the node is empty or the node data is equal to data that i have give
        if self.root is None or root.item == data:
            return None
        
        # secod case if the data is smaller than  root data 
        if data < root.item:
            return self._search_recursive(root.left, data)
        else:
            return self._search_recursive(root.right, data)
        

            
    

        
                
            
            
               
            




            
                

                
            
            

            
                

                

            






                








            

            

