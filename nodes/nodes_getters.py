"""  
NODES PYTHON GETTERS ----------------------------------------------------->
We need methods to access the data and link within the node. For this, we 
will use two getters, .get_value() and .get_link_node(). These should 
each return their corresponding value on the self object.
"""

class Node:
    def __init__(self, value, link_node = None):
        self.value = value
        self.link_node = link_node

    def get_value(self):
        return self.value
    
    def get_link_node(self):
        return self.link_node

        
